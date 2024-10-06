import time
import numpy as np
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from scipy.signal import butter, lfilter, iirnotch


class EEGProcessor:
    def __init__(self):
        # Initialize BrainFlow
        BoardShim.enable_dev_board_logger()
        params = BrainFlowInputParams()
        self.board_id = BoardIds.SYNTHETIC_BOARD.value
        self.board = BoardShim(self.board_id, params)
        self.board.prepare_session()
        self.board.start_stream()
        print("BrainFlow streaming started...")

        # Sampling rate and window size
        self.sampling_rate = BoardShim.get_sampling_rate(self.board_id)
        self.window_size_sec = 1.5  # seconds
        self.window_size_samples = int(self.window_size_sec * self.sampling_rate)

        # we set raw window size to 10 seconds (why?)
        self.window_size_raw = int(10 * self.sampling_rate)
        self.lowcut = 1.0
        self.highcut = 50.0
        self.notch = 60.0

        # Get EEG channels
        self.eeg_channels = BoardShim.get_eeg_channels(self.board_id)

        # Initialize buffers
        self.raw_data_buffer = np.empty((len(self.eeg_channels), 0))
        self.processed_data_buffer = np.empty((len(self.eeg_channels), 0))

    def stop(self):
        # Stop the data stream and release the session
        self.board.stop_stream()
        self.board.release_session()
        print("BrainFlow streaming stopped.")

    def get_recent_data(self):
        """
        Returns the most recent 1.5 seconds of processed EEG data.

        The data is bandpass filtered, notch filtered, and z-scored.
        Each data point is filtered only once.
        """
        data = self.board.get_board_data() 
        if data.shape[1] == 0:
            # No new data
            pass
        else:
            # Append new raw data to the raw_data_buffer
            eeg_data = data[self.eeg_channels, :]
            self.raw_data_buffer = np.hstack((self.raw_data_buffer, eeg_data))

            # Process new data
            new_processed_data = np.empty(self.raw_data_buffer.shape)
            # It is important to process each channel separately (why?)
            for i in range(len(self.eeg_channels)):

                # it is important to use the whole buffer for filtering (why?)
                # Get the channel data
                channel_data = self.raw_data_buffer[i, :].copy()

                # Bandpass filter
                b, a = butter(2, [self.lowcut, self.highcut], btype='band', fs=self.sampling_rate)
                channel_data = lfilter(b, a, channel_data)
                
                # Notch filter
                b, a = iirnotch(self.notch, 30, fs=self.sampling_rate)
                channel_data = lfilter(b, a, channel_data)

                # Z-score
                mean = np.mean(channel_data)
                std = np.std(channel_data)
                if std == 0:
                    std = 1  
                channel_data = (channel_data - mean) / std
                # add channel dimension to channel_data
                new_processed_data[i, :] =  channel_data

            
            self.processed_data_buffer = np.hstack((self.processed_data_buffer, new_processed_data))

            max_buffer_size = self.window_size_samples * 2
            if self.raw_data_buffer.shape[1] > self.window_size_raw:
                self.raw_data_buffer = self.raw_data_buffer[:, -self.window_size_raw:]
            if self.processed_data_buffer.shape[1] > max_buffer_size:
                self.processed_data_buffer = self.processed_data_buffer[:, -max_buffer_size:]

        if self.processed_data_buffer.shape[1] >= self.window_size_samples:
            recent_data = self.processed_data_buffer[:, -self.window_size_samples:]
        else:
            recent_data = self.processed_data_buffer

        return recent_data

def main():
    eeg_processor = EEGProcessor()
    time.sleep(2) # wait until we can fill the buffer (why?)

    try:
        while True:
            start_time = time.time()
            recent_data = eeg_processor.get_recent_data()
            print("Recent data shape:", recent_data.shape)
            # Do something with recent_data
            print("Recent data shape:", recent_data.shape)
            # We want to process data 10 times a second (why?)
            elapsed_time = time.time() - start_time
            sleep_time = max(0, 0.1 - elapsed_time)
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        eeg_processor.stop()

if __name__ == "__main__":
    main()
