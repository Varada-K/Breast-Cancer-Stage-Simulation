# Project

## Question: 
What is the cost-effectiveness of breast conservative surgery compared to combined surgery and radiation therapy in women with early and locally advanced breast cancer?

## Understanding the Disease
- Sequential progression of disease:
  - Stage 0 and 1: Early stages
  - Stage 2 and 3: Locally advanced tumor
  - Stage 4: Metastasis stage
- Treatment modalities:
  - Surgery
  - Radiation therapy
  - Chemotherapy
  - Other therapies
 
## Natural Progression of Breast Cancer

<img width="450" alt="image" src="https://github.com/Varada-K/Breast-Cancer-Stage-Simulation/assets/144185938/92c8b551-cd34-40e4-8dca-1b7a407cf692">

## Solution Method
- Discrete Time Markov Model
- Focuses on Surgery and Radiation Therapy
- Surgery preferred in early stages, before spread
  - Modeled by adjusting transition probabilities
  - Lowers risk of recurrence
- Radiation therapy often conducted after surgery to kill cancer
  - Modeled by increasing the probability of staying in the same stage
  - Enhances "local control"
    
## Modelling Approach 
<img width="356" alt="image" src="https://github.com/Varada-K/Breast-Cancer-Stage-Simulation/assets/144185938/9121a81c-3498-4db3-90e7-e5ea306919c0">

