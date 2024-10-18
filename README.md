## LLM Application Write Up

### Introduction
This project contains some middleware to connect end-users to the Donovan LLM model and uses a RAG technique to evaluate municipal data. 
As a governmental entity, you can spend an absurd amount of time and money establishing priority of feedback or reports from citizens. This project seeks to address that issue. Even large cities have used LLMs to solve approach big issues. I mention these both as the inspiration for the project but I would also use these examples to reinforce the value proposition when approaching clients. 

- Los Angeles, CA - Optimizing Traffic Management using a RAG to consider effects of weather, events, and public transport data using historical data and forecasts
- Chicago, IL - AI for Predictive Analytics has helped identify buildings at high risk of lead contamination; a RAG could refine predictions by with added data and offer interventions.
- New Yock City, NY - New Yorks 311 System is no powered by AI and categorizes and routes requests. It's not a full RAG but has steamlined the process. 

Analyzing 311 Service Requests data using a RAG takes the efforts of New York City one step further.

### REPO
In this repo you'll find a few items that helped me explore donovan and expand my knowledge of Scales product. I felt that setting up a new dataset was key in getting the full donovan experience even though the instructions said it was not necessary. 
- module donovan_interaction.py that via keyword arguments will help the user explore datasets, workspaces, and models
- module chat.py that includes several functions for chatting with LLM models
- the requirements file for some python libraries used (as a pip freeze it is lengthy)
- 311 Service Call data from the opendata.dc.gov project that was sent to the workspace dataset
    - the main geojson and the ward_data directory where there is a json that contains the data for each was (processing/posting the main file was a little heavy with ~350k records)

### More On the Problem
In this section I'd like to discuss how I would approach a customer in this scenario.

First, my team and I would conduct and extensive needs analysis / discovery period. Normally, when working with private sector clients, you have to be clear about how the objectives of the project directly affect the business goals of the customer, aka "**how will this affect my bottom line**" and "**how will it make us money?**" A government doesn't make money like a private institution. What they do care about, overwhelmingly, is getting re-elected and mitigating risk and further unnecessary cost. These are the outcomes we would have to make from the onset of the relationship:
- Your constituents will feel their concerns have been heard. Satisfaction and improved quality of life will be take place.
- Dealing with the most frequent and pressing issues first will: 
    - avoid costly program repairs later on
    - mitigate threats/risks to the citizenry

Furthermore, working with Scale.ai and our proprietary technology will save countless hours of meetings and deliberation about what problems to approach and how. 

I have constructed some prompts that during discovery could yield results that present real tangible value to the customer:

- "What is the most common 311 service request in the DC Metro Area" (DataSet Sample)
- "Analyze the types of service requests the dataset. Which service request would be the easiest to remedy compared to its severity?"
- "Are there hot spots or specific areas of concern that should be addressed first? Name three of these areas and provide a summary of the requests." 
- "Based on the customer service requests from 2024, what are reasonable predictions for requests in 2025?"

Such questions could help pinpoint current and future trends; these analyses, courtesy of LLM/RAG could help with budget allocation and priorities for the future of the administration on top of help with the aforementioned. 

### If I Had A Few Weeks
I would expand on the results and successes of AI/RAG programs launched in cities/municipalities. I would create an interactive and intriguing presentation (preferably without using PowerPoint) to hammer home the benefits of working with Scale on this matter but also the pitfalls of alternative approaches, say costly and unreliable DIY methods.
If I had a contract with a municipality... and the results of a deep discovery period... and a small team of developers, I would design an intuitive, web-hosted, data-exploration tool and dashboard with easily digestible infographics and report printing capabilities. The tool would arm the customers with the data they need to confidently approach a higher standard of living for their citizenry and take as much of the tedium and guess work out of governance as possible.



