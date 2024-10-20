# Weekly Responsibilities Overview

## Project Lead: Jayanth Damodaran

### Teams Under Leadership
- **ML Interpretibility**
- **ML Development 1 (Matthew)**
- **ML Development 2 (Miran)**

---

### All Teams
- Complete onboarding
    - Finish up with the ML competition (either house price or BCI Motor Imagery)
    - send notebooks and presentations to Project Lead (Jay)
- Since data acquisition is beginning for prosthetic arm project, we need to ensure CapsNet and training script are ready for prediction on this data (shouldn't be too much work, mainly using existing code from Nathan)
- Use UT box to hold papers and models that you all find for your groups as you read about new/improved MI Classification Models

---

### ML Interpretibility
**Objective:** 
Optimize Capsule Network including experimenting with model parameters to increase accuracy or reduce size of model.

**Understanding CapsNet**
- search literature to collect as many useful papers on CapsNet as you all can find
    - preferably find papers on BCI applications of CapsNet
- read through papers and go over them as a group to understand CapsNet architecture
- find best implementations of CapsNet and try to understand
- examine CapsNet code provided by Nathan (Software Lead) and run script
    - code is found in BCIPong private repository in LonghornNeurotech github

**Modifying CapsNet**
- try changing kernel sizes in convolutional layers
- try using different number of capsules
- see if you can modify inputs like feeding in frequency domain or time-frequency data 

---

### ML Development 1 (Matthew)
**Objective:**  
Implement new end to end ML model architectures trying to outperform baseline provided by CapsNet, either in terms of accuracy or speed. 

**1. Finish Presentations**
Work on ML competition in this Sunday's meeting and prepare for your presentations on Tuesday. Jay will be there for your presentations

**2. Finding New Models**
Examine literature to find new models to implement for eeg or time series classification. Create spreadsheet along with ML Development team 2 (like in google sheets) with models and information about their performance and whether they have been used for motor imagery applications. A prior spreadsheet will be provided. 

**3. Dividing Work**
Work with Miran to divy up work on model implementation from the shared spreadsheet and ensure both teams aren't working on redundant models

**4. Tips for implementing New Models**
- find papers that break down models layer by layer and try to implement based on that
- look for github repositories that show model implementation and adapt that
- ask ChatGPT for help with Pytorch implementation
- work together (such as paired programming)

**5. Evaluating Models**
- Use either the BCI competition 4 2a dataset or Nathan's eeg dataset which will be provided

---

## ML Development 2 (Miran)
**Objective:**  
Implement new end to end ML model architectures trying to outperform baseline provided by CapsNet, either in terms of accuracy or speed. 

**1. Finding New Models**
Examine literature to find new models to implement for eeg or time series classification. Create spreadsheet along with ML Development team 1 (like in google sheets) with models and information about their performance and whether they have been used for motor imagery applications. A prior spreadsheet will be provided. 
   
**3. Dividing Work**
Work with Matthew to divy up work on model implementation from the shared spreadsheet and ensure both teams aren't working on redundant models

**3. Tips for implementing New Models**
- find papers that break down models layer by layer and try to implement based on that
- look for github repositories that show model implementation and adapt that
- ask ChatGPT for help with Pytorch implementation
- work together (such as paired programming)

**4. Evaluating Models**
- Use either the BCI competition 4 2a dataset or Nathan's eeg dataset which will be provided

---

## Recap of Other Teams

- **UI/UX:**  
  Improving the data collection GUI design. Collaboration with RT Signals is essential to resolve any overlapping issues.

- **Signals:**
  Developed RT data collection pipeline for data collection beginning (10/20/24)

- **VR Team:**  
  Developing the interface for the 6 degrees of freedom model.

---

## Looking Forward

- **Finalizing Data Collection GUI:**  
    Once the GUI is finalized, no further changes will be made until data collection is complete to maintain consistency across trials.
    Collected data will be found in the box. 

- **ML Interpretability**  
  Continue experimenting with CapsNet model (perhaps team can be divided into two groups, suggestions below)
    - one group can modify CapsNet hyperparameters and training script while the other can make more dramatic changes with the architecture such as adding or deleting layers
    - one group can focus on model optimization while another can focus on model interpretation

- **ML Development 1 and 2**  
    Research to find new models and start adding information about them in shared spreadsheet, then start implementing them after dividing up the work between the two subteams. I understand model development is a long and challenging process, and I don't expect you all to come up with a state of the art model each week, but I do want to see time spent working on this. By the end of this week, ML should have newly collected data to work with. 

---