# True Evolutionary AGI 
[![Python Version](https://img.shields.io/badge/Python-3.9-blue.svg)](https://github.com/MineDojo/Voyager)
[![GitHub license](https://img.shields.io/github/license/MineDojo/Voyager)](https://github.com/MineDojo/Voyager/blob/main/LICENSE)
## Motivation
Inspired by Voyager - the first LLM-powered embodied lifelong learning agent in Minecraft that continuously explores the world.
However Minecraft is an API driven virtual digital world, when it comes to real world can I reproduce the same?

In this project, I take an initial step towards enabling general tools making skills for AGI to have LLM create their own reusable tools for problem-solving in the real world.

It will be a self-study AI capable of solving complex challenges. Its ability will grow stronger over time, and this evolutionary process should rely on minimum code only. AI will write code for self-enhancement and enrich its library tools.

There are some key features I would like to empower AI:

1. Decompose the complex goal into sub-goals, further breakdown sub-goals into tasks.

2. Task execution depends on tool selection, action agent will retrieve proper tools from library. If none of the tools available for specified task, AI should build one with coding.

3. If task execution is passed, add this new tool into library, otherwise fix the issue by critic agent.

When AI has any doubt during the entire process, it should interact with humans for assistance or confirmation.

## Key Components
Goal Decomposition: This component will be responsible for breaking down the complex goal into sub-goals and further breaking down sub-goals into tasks. Consider hierarchical task network (HTN) planner to achieve this. The HTN planner will take the high-level goal and decompose it into smaller sub-goals, which can be further decomposed into tasks.

Tool Selection: This component will be responsible for selecting the appropriate tools from the library for executing the tasks. Tool script and description will be embedded into vector DB as value and key for future retrieval.

Tool Library: This component will store all the tools that the AI has learned. The tools will be organized based on their functionality and complexity. The AI will add new tools to the library when it successfuly creates them.

Critic Agent: This component will be responsible for evaluating the performance of the AI. If the task execution fails, the critic agent will provide feedback to the AI, which will use this feedback to improve its performance. 

Human Interaction: This component will allow the AI to interact with humans when it has doubts or needs assistance. 
