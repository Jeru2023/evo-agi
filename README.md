# True Evolutionary AGI 
[![Python Version](https://img.shields.io/badge/Python-3.9-blue.svg)](https://github.com/MineDojo/Voyager)
[![GitHub license](https://img.shields.io/github/license/MineDojo/Voyager)](https://github.com/MineDojo/Voyager/blob/main/LICENSE)
## Motivation
Inspired by Voyager - the first LLM-powered embodied lifelong learning agent in Minecraft that continuously explores the world.
However Minecraft is an API driven virtual digital world, when it comes to real world can I reproduce the same?

In this project, I take an initial step towards enabling general tools making skills for AGI to have LLM create their own reusable tools for problem-solving in the real world.

## Key Components
Goal Decomposition: This component will be responsible for breaking down the complex goal into sub-goals and further breaking down sub-goals into tasks. You can use a hierarchical task network (HTN) planner to achieve this. The HTN planner will take the high-level goal and decompose it into smaller sub-goals, which can be further decomposed into tasks.

Tool Selection: This component will be responsible for selecting the appropriate tools from the library for executing the tasks. You can use a rule-based system or a decision tree to select the tools. If none of the tools are available for a specified task, the AI should build one with coding. You can use a genetic algorithm or a neural network to generate the code for the new tool.

Tool Library: This component will store all the tools that the AI has learned. The tools will be organized based on their functionality and complexity. The AI will add new tools to the library when it creates them.

Critic Agent: This component will be responsible for evaluating the performance of the AI. If the task execution fails, the critic agent will provide feedback to the AI, which will use this feedback to improve its performance. You can use a reinforcement learning algorithm to train the critic agent.

Human Interaction: This component will allow the AI to interact with humans when it has doubts or needs assistance. You can use a chatbot or a voice assistant to facilitate the interaction.
