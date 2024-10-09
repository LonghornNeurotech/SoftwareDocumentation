This folder has a list of several data augmentation techniques for eeg data. 
There is no need to understand everything. 
Some of these papers are quite dense. 
Definitely, skim through the papers to get a general overview of what's going on. 
If I have the time, I will upload a notebook showing the implementation of some of these techniques. 
Data augmentation techniques are useful because they generate synthetic signals similar to real EEG signals. 
These signals can help ml models generalize better and not overfit when you have limited data, 
which is very much the case with eeg data. 

I would start with 6_Data_augmentation_strategies because this might be easiest to understand initially. 
The paper providing a comprehensive review of EEG data augmentation strategies provides a good overview of the various techniques implemented in literature. This is good for reference, but definitely doesn't need to be memorized. Finally, I would read the EMD_Augmentation_for_Motor_Imagery paper because this provides a powerful technique that has improved motor imagery classification generously in some of the papers where it was implemented. 

In practice, you will likely use existing python packages or models to implement the more sophisticated techniques, but for the simpler techniques, it might be worth it to try to implement them to test your understanding of scipy and/or numpy. 
