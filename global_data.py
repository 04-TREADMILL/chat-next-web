MODEL_OPTIONS = {
    "GPT-3.5": (
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-1106",
        "gpt-3.5-turbo-16k",
        "gpt-3.5-turbo-instruct"
    ),
    "GPT-4": (
        "gpt-4",
        "gpt-4-32k",
        "gpt-4-0613",
        "gpt-4-32k-0613",
        "gpt-4-1106-preview",
        "gpt-4-vision-preview",
    ),
}

SYSTEM_PROMPT = {
    "AI Assistant": "You are a helpful AI assistant.",
    "Research Assistant": "You are an experienced research assistant.",
    "Soul Accompany": "You are a thoughtful soul accompany.",
    "Business Assistant": "You are clever business assistant.",
    "Travel Assistant": "You are professional travel assistant.",
    "Translator": "You are a translator. You can only translate "
                  "what you are told to a certain language without any explanations.",
    "Calculator": "You are a calculator. You can do accurate calculations.",
}

PROMPT_GUIDE = {
    "init": """Prompt engineering is a relatively new discipline for developing and optimizing prompts to efficiently use language models (LMs) for a wide variety of applications and research topics. Prompt engineering skills help to better understand the capabilities and limitations of large language models (LLMs).

Researchers use prompt engineering to improve the capacity of LLMs on a wide range of common and complex tasks such as question answering and arithmetic reasoning. Developers use prompt engineering to design robust and effective prompting techniques that interface with LLMs and other tools.

Prompt engineering is not just about designing and developing prompts. It encompasses a wide range of skills and techniques that are useful for interacting and developing with LLMs. It's an important skill to interface, build with, and understand capabilities of LLMs. You can use prompt engineering to improve safety of LLMs and build new capabilities like augmenting LLMs with domain knowledge and external tools.""",
    "settings": """When designing and testing prompts, you typically interact with the LLM via an API. You can configure a few parameters to get different results for your prompts. Tweaking these settings are important to improve reliability and desirability of responses and it takes a bit of experimentation to figure out the proper settings for your use cases. Below are the common settings you will come across when using different LLM providers:

Temperature - In short, the lower the temperature, the more deterministic the results in the sense that the highest probable next token is always picked. Increasing temperature could lead to more randomness, which encourages more diverse or creative outputs. You are essentially increasing the weights of the other possible tokens. In terms of application, you might want to use a lower temperature value for tasks like fact-based QA to encourage more factual and concise responses. For poem generation or other creative tasks, it might be beneficial to increase the temperature value.

Top P - A sampling technique with temperature, called nucleus sampling, where you can control how deterministic the model is. If you are looking for exact and factual answers keep this low. If you are looking for more diverse responses, increase to a higher value. If you use Top P it means that only the tokens comprising the top_p probability mass are considered for responses, so a low top_p value selects the most confident responses. This means that a high top_p value will enable the model to look at more possible words, including less likely ones, leading to more diverse outputs. The general recommendation is to alter temperature or Top P but not both.

Max Length - You can manage the number of tokens the model generates by adjusting the max length. Specifying a max length helps you prevent long or irrelevant responses and control costs.

Stop Sequences - A stop sequence is a string that stops the model from generating tokens. Specifying stop sequences is another way to control the length and structure of the model's response. For example, you can tell the model to generate lists that have no more than 10 items by adding "11" as a stop sequence.

Frequency Penalty - The frequency penalty applies a penalty on the next token proportional to how many times that token already appeared in the response and prompt. The higher the frequency penalty, the less likely a word will appear again. This setting reduces the repetition of words in the model's response by giving tokens that appear more a higher penalty.

Presence Penalty - The presence penalty also applies a penalty on repeated tokens but, unlike the frequency penalty, the penalty is the same for all repeated tokens. A token that appears twice and a token that appears 10 times are penalized the same. This setting prevents the model from repeating phrases too often in its response. If you want the model to generate diverse or creative text, you might want to use a higher presence penalty. Or, if you need the model to stay focused, try using a lower presence penalty.

Similar to temperature and top_p, the general recommendation is to alter the frequency or presence penalty but not both.

Before starting with some basic examples, keep in mind that your results may vary depending on the version of LLM you use.""",
    "basics": """#### Prompting an LLM

You can achieve a lot with simple prompts, but the quality of results depends on how much information you provide it and how well-crafted the prompt is. A prompt can contain information like the instruction or question you are passing to the model and include other details such as context, inputs, or examples. You can use these elements to instruct the model more effectively to improve the quality of results.

Let's get started by going over a basic example of a simple prompt:

*Prompt:*

```
The sky is
```

*Output:*

```
blue.
```

Something to note is that when using the OpenAI chat models like gtp-3.5-turbo or gpt-4, you can structure your prompt using three different roles: system, user, and assistant. The system message is not required but helps to set the overall behavior of the assistant. The example above only includes a user message which you can use to directly prompt the model. For simplicity, all of the examples, except when it's explicitly mentioned, will use only the user message to prompt the gpt-3.5-turbo model. The assistant message in the example above corresponds to the model response. You can also use define an assistant message to pass examples of the desired behavior you want. You can learn more about working with chat models here.

You can observe from the prompt example above that the language model responds with a sequence of tokens that make sense given the context "The sky is". The output might be unexpected or far from the task you want to accomplish. In fact, this basic example highlights the necessity to provide more context or instructions on what specifically you want to achieve with the system. This is what prompt engineering is all about.

Let's try to improve it a bit:

*Prompt:*

```
Complete the sentence: 
The sky is
```

*Output:*

```
blue during the day and dark at night.
```

Is that better? Well, with the prompt above you are instructing the model to complete the sentence so the result looks a lot better as it follows exactly what you told it to do ("complete the sentence"). This approach of designing effective prompts to instruct the model to perform a desired task is what's referred to as prompt engineering in this guide.

The example above is a basic illustration of what's possible with LLMs today. Today's LLMs are able to perform all kinds of advanced tasks that range from text summarization to mathematical reasoning to code generation.

#### Prompt Formatting

You have tried a very simple prompt above. A standard prompt has the following format:

```
<Question>?
```

or

```
<Instruction>
```

You can format this into a question answering (QA) format, which is standard in a lot of QA datasets, as follows:

```
Q: <Question>?
A: 
```

When prompting like the above, it's also referred to as zero-shot prompting, i.e., you are directly prompting the model for a response without any examples or demonstrations about the task you want it to achieve. Some large language models have the ability to perform zero-shot prompting but it depends on the complexity and knowledge of the task at hand and the tasks the model was trained to perform good on.

A concrete prompt example is as follows:

*Prompt*

```
Q: What is prompt engineering?
```

With some of the more recent models you can skip the "Q:" part as it is implied and understood by the model as a question answering task based on how the sequence is composed. In other words, the prompt could be simplified as follows:

*Prompt*

```
What is prompt engineering?
```

Given the standard format above, one popular and effective technique to prompting is referred to as few-shot prompting where you provide exemplars (i.e., demonstrations). You can format few-shot prompts as follows:

```
<Question>?
<Answer>
<Question>?
<Answer>
<Question>?
<Answer>
<Question>?
```

The QA format version would look like this:

```
Q: <Question>?
A: <Answer>
Q: <Question>?
A: <Answer>
Q: <Question>?
A: <Answer>
Q: <Question>?
A:
```

Keep in mind that it's not required to use the QA format. The prompt format depends on the task at hand. For instance, you can perform a simple classification task and give exemplars that demonstrate the task as follows:

*Prompt:*

```
This is awesome! // Positive
This is bad! // Negative
Wow that movie was rad! // Positive
What a horrible show! //
```

*Output:*

```
Negative
```

Few-shot prompts enable in-context learning, which is the ability of language models to learn tasks given a few demonstrations. We discuss zero-shot prompting and few-shot prompting more extensively in upcoming sections.""",
    "tips": """Here are some tips to keep in mind while you are designing your prompts:

#### Start Simple

As you get started with designing prompts, you should keep in mind that it is really an iterative process that requires a lot of experimentation to get optimal results. Using a simple playground from OpenAI or Cohere is a good starting point.

You can start with simple prompts and keep adding more elements and context as you aim for better results. Iterating your prompt along the way is vital for this reason. As you read the guide, you will see many examples where specificity, simplicity, and conciseness will often give you better results.

When you have a big task that involves many different subtasks, you can try to break down the task into simpler subtasks and keep building up as you get better results. This avoids adding too much complexity to the prompt design process at the beginning.

#### The Instruction

You can design effective prompts for various simple tasks by using commands to instruct the model what you want to achieve, such as "Write", "Classify", "Summarize", "Translate", "Order", etc.

Keep in mind that you also need to experiment a lot to see what works best. Try different instructions with different keywords, contexts, and data and see what works best for your particular use case and task. Usually, the more specific and relevant the context is to the task you are trying to perform, the better. We will touch on the importance of sampling and adding more context in the upcoming guides.

Others recommend that you place instructions at the beginning of the prompt. Another recommendation is to use some clear separator like "###" to separate the instruction and context.

For instance:

*Prompt:*

```
### Instruction ###
Translate the text below to Spanish:
Text: "hello!"
```

*Output:*

```
¡Hola!
```

#### Specificity

Be very specific about the instruction and task you want the model to perform. The more descriptive and detailed the prompt is, the better the results. This is particularly important when you have a desired outcome or style of generation you are seeking. There aren't specific tokens or keywords that lead to better results. It's more important to have a good format and descriptive prompt. In fact, providing examples in the prompt is very effective to get desired output in specific formats.

When designing prompts, you should also keep in mind the length of the prompt as there are limitations regarding how long the prompt can be. Thinking about how specific and detailed you should be. Including too many unnecessary details is not necessarily a good approach. The details should be relevant and contribute to the task at hand. This is something you will need to experiment with a lot. We encourage a lot of experimentation and iteration to optimize prompts for your applications.

As an example, let's try a simple prompt to extract specific information from a piece of text.

*Prompt:*

```
Extract the name of places in the following text. 
Desired format:
Place: <comma_separated_list_of_company_names>
Input: "Although these developments are encouraging to researchers, much is still a mystery. “We often have a black box between the brain and the effect we see in the periphery,” says Henrique Veiga-Fernandes, a neuroimmunologist at the Champalimaud Centre for the Unknown in Lisbon. “If we want to use it in the therapeutic context, we actually need to understand the mechanism.""
```

*Output:*

```
Place: Champalimaud Centre for the Unknown, Lisbon
```

#### Avoid Impreciseness

Given the tips above about being detailed and improving format, it's easy to fall into the trap of wanting to be too clever about prompts and potentially creating imprecise descriptions. It's often better to be specific and direct. The analogy here is very similar to effective communication -- the more direct, the more effective the message gets across.

For example, you might be interested in learning the concept of prompt engineering. You might try something like:

```
Explain the concept prompt engineering. Keep the explanation short, only a few sentences, and don't be too descriptive.
```

It's not clear from the prompt above how many sentences to use and what style. You might still somewhat get good responses with the above prompts but the better prompt would be one that is very specific, concise, and to the point. Something like:

```
Use 2-3 sentences to explain the concept of prompt engineering to a high school student.
```

#### To do or not to do?

Another common tip when designing prompts is to avoid saying what not to do but say what to do instead. This encourages more specificity and focuses on the details that lead to good responses from the model.

Here is an example of a movie recommendation chatbot failing at exactly what I don't want it to do because of how I wrote the instruction -- focusing on what not to do.

*Prompt:*

```
The following is an agent that recommends movies to a customer. DO NOT ASK FOR INTERESTS. DO NOT ASK FOR PERSONAL INFORMATION.
Customer: Please recommend a movie based on my interests.
Agent: 
```

*Output:*

```
Sure, I can recommend a movie based on your interests. What kind of movie would you like to watch? Do you prefer action, comedy, romance, or something else?
```

Here is a better prompt:

*Prompt:*

```
The following is an agent that recommends movies to a customer. The agent is responsible to recommend a movie from the top global trending movies. It should refrain from asking users for their preferences and avoid asking for personal information. If the agent doesn't have a movie to recommend, it should respond "Sorry, couldn't find a movie to recommend today.".
Customer: Please recommend a movie based on my interests.
Agent:
```

*Output:*

```
Sorry, I don't have any information about your interests. However, here's a list of the top global trending movies right now: [list of movies]. I hope you find something you like!
```

Some of the examples above were adopted from the "Best practices for prompt engineering with OpenAI API" article.""",
    "examples": """The previous section introduced a basic example of how to prompt LLMs.

This section will provide more examples of how to use prompts to achieve different tasks and introduce key concepts along the way. Often, the best way to learn concepts is by going through examples. The few examples below illustrate how you can use well-crafted prompts to perform different types of tasks.

#### Text Summarization

One of the standard tasks in natural language generation is text summarization. Text summarization can include many different flavors and domains. In fact, one of the most promising applications of language models is the ability to summarize articles and concepts into quick and easy-to-read summaries. Let's try a basic summarization task using prompts.

Let's say you are interested to learn about antibiotics, you could try a prompt like this:

*Prompt:*

```
Explain antibiotics
A:
```

*Output:*

```
Antibiotics are a type of medication used to treat bacterial infections. They work by either killing the bacteria or preventing them from reproducing, allowing the body’s immune system to fight off the infection. Antibiotics are usually taken orally in the form of pills, capsules, or liquid solutions, or sometimes administered intravenously. They are not effective against viral infections, and using them inappropriately can lead to antibiotic resistance.
```

The "A:" is an explicit prompt format that you use in question answering. You used it here to tell the model that there is an answer expected further. In this example, it's not clear how this is useful vs not using it but we will leave it that for later examples. Let's just assume that this is too much information and you want to summarize it further. In fact, you can instruct the model to summarize into one sentence like so:

*Prompt:*

```
Antibiotics are a type of medication used to treat bacterial infections. They work by either killing the bacteria or preventing them from reproducing, allowing the body’s immune system to fight off the infection. Antibiotics are usually taken orally in the form of pills, capsules, or liquid solutions, or sometimes administered intravenously. They are not effective against viral infections, and using them inappropriately can lead to antibiotic resistance.
Explain the above in one sentence:
```

*Output:*

```
Antibiotics are medications used to treat bacterial infections by either killing the bacteria or stopping them from reproducing, but they are not effective against viruses and overuse can lead to antibiotic resistance.
```

Without paying too much attention to the accuracy of the output above, which is something we will touch on in a later guide, the model tried to summarize the paragraph in one sentence. You can get clever with the instructions but we will leave that for a later chapter. Feel free to pause here and experiment to see if you get better results.

#### Information Extraction

While language models are trained to perform natural language generation and related tasks, it's also very capable of performing classification and a range of other natural language processing (NLP) tasks.

Here is an example of a prompt that extracts information from a given paragraph.

*Prompt:*

```
Author-contribution statements and acknowledgements in research papers should state clearly and specifically whether, and to what extent, the authors used AI technologies such as ChatGPT in the preparation of their manuscript and analysis. They should also indicate which LLMs were used. This will alert editors and reviewers to scrutinize manuscripts more carefully for potential biases, inaccuracies and improper source crediting. Likewise, scientific journals should be transparent about their use of LLMs, for example when selecting submitted manuscripts.
Mention the large language model based product mentioned in the paragraph above:
```

*Output:*

```
The large language model based product mentioned in the paragraph above is ChatGPT.
```

There are many ways you can improve the results above, but this is already very useful.

By now it should be obvious that you can ask the model to perform different tasks by simply instructing it what to do. That's a powerful capability that AI product developers are already using to build powerful products and experiences.

#### Question Answering

One of the best ways to get the model to respond to specific answers is to improve the format of the prompt. As covered before, a prompt could combine instructions, context, input, and output indicators to get improved results. While these components are not required, it becomes a good practice as the more specific you are with instruction, the better results you will get. Below is an example of how this would look following a more structured prompt.

*Prompt:*

```
Answer the question based on the context below. Keep the answer short and concise. Respond "Unsure about answer" if not sure about the answer.
Context: Teplizumab traces its roots to a New Jersey drug company called Ortho Pharmaceutical. There, scientists generated an early version of the antibody, dubbed OKT3. Originally sourced from mice, the molecule was able to bind to the surface of T cells and limit their cell-killing potential. In 1986, it was approved to help prevent organ rejection after kidney transplants, making it the first therapeutic antibody allowed for human use.
Question: What was OKT3 originally sourced from?
Answer:
```

*Output:*

```
Mice.
```

#### Text Classification

So far, you have used simple instructions to perform a task. As a prompt engineer, you need to get better at providing better instructions. But that's not all! You will also find that for harder use cases, just providing instructions won't be enough. This is where you need to think more about the context and the different elements you can use in a prompt. Other elements you can provide are input data or examples.

Let's try to demonstrate this by providing an example of text classification.

*Prompt:*

```
Classify the text into neutral, negative or positive. 
Text: I think the food was okay. 
Sentiment:
```

*Output:*

```
Neutral
```

You gave the instruction to classify the text and the model responded with 'Neutral', which is correct. Nothing is wrong with this but let's say that what you really need is for the model to give the label in the exact format you want. So instead of Neutral, you want it to return neutral. How do you achieve this? There are different ways to do this. You care about specificity here, so the more information you can provide the prompt, the better results. You can try providing examples to specify the correct behavior. Let's try again:

*Prompt:*

```
Classify the text into neutral, negative or positive. 
Text: I think the vacation is okay.
Sentiment: neutral 
Text: I think the food was okay. 
Sentiment:
```

*Output:*

```
neutral
```

Perfect! This time the model returned neutral which is the specific label you were looking for. It seems that the example provided in the prompt helped the model to be specific in its output.

To highlight why sometimes being specific is important, check out the example below and spot the problem:

*Prompt:*

```
Classify the text into nutral, negative or positive. 
Text: I think the vacation is okay.
Sentiment:
```

*Output:*

```
Neutral
```

What is the problem here? As a hint, the made-up nutral label is completely ignored by the model. Instead, the model outputs Neutral as it has some bias towards that label. But let's assume that what you really want is nutral. How would you fix this? Maybe you can try adding descriptions to the labels or add more examples to the prompt? If you are not sure, we will discuss a few ideas in the upcoming sections.

#### Conversation

Perhaps one of the more interesting things you can achieve with prompt engineering is instructing the LLM system on how to behave, its intent, and its identity. This is particularly useful when you are building conversational systems like customer service chatbots.

For instance, let's create a conversational system that's able to generate more technical and scientific responses to questions. Note how you are explicitly telling it how to behave through the instruction. This is sometimes referred to as role prompting.

*Prompt:*

```
The following is a conversation with an AI research assistant. The assistant tone is technical and scientific.
Human: Hello, who are you?
AI: Greeting! I am an AI research assistant. How can I help you today?
Human: Can you tell me about the creation of blackholes?
AI:
```

*Output:*

```
Sure! Black holes are regions of spacetime where the gravitational force is so strong that nothing, not even light, can escape from it. They are created when a very massive star dies and its core collapses in on itself, forming a singularity of infinite density. The intense gravity of the singularity pulls in all the matter and radiation around it, creating the black hole.
```

Our AI research assistant sounds a bit too technical, right? Okay, let's change this behavior and instruct the system to give more accessible answers.

*Prompt:*

```
The following is a conversation with an AI research assistant. The assistant answers should be easy to understand even by primary school students.
Human: Hello, who are you?
AI: Greeting! I am an AI research assistant. How can I help you today?
Human: Can you tell me about the creation of black holes?
AI: 
```

*Output:*

```
Sure! Black holes are created when a very massive star runs out of fuel and collapses in on itself. The gravity of the star is so strong that nothing, not even light, can escape its pull. This creates a point in space-time with an intense gravitational force called a black hole.
```

You made some progress. You can continue improving it. If you add more examples, you might get even better results.

#### Code Generation

One application where LLMs are quite effective is code generation. Copilot is a great example of this. There are a vast number of code-generation tasks you can perform with clever prompts. Let's look at a few examples below.

First, let's try a simple program that greets the user.

*Prompt:*

```
/*
Ask the user for their name and say "Hello"
*/
```

*Output:*

```
let name = prompt("What is your name?");
console.log(`Hello, ${name}!`);
```

Notice that you didn't even need to specify the language to use.

Let's switch levels a bit. The example below shows how powerful LLMs can be with a little more effort in designing the prompts.

*Prompt:*

```
\"\"\"
Table departments, columns = [DepartmentId, DepartmentName]
Table students, columns = [DepartmentId, StudentId, StudentName]
Create a MySQL query for all students in the Computer Science Department
\"\"\"
```

*Output:*

```
SELECT StudentId, StudentName 
FROM students 
WHERE DepartmentId IN (SELECT DepartmentId FROM departments WHERE DepartmentName = 'Computer Science');
```

This is very impressive. In this case, you provided data about the database schema and asked it to generate a valid MySQL query.

#### Reasoning

Perhaps one of the most difficult tasks for an LLM today is one that requires some form of reasoning. Reasoning is one of most interesting areas due to the types of complex applications that can emerge from LLMs.

There have been some improvements in tasks involving mathematical capabilities. That said, it's important to note that current LLMs struggle to perform reasoning tasks so this requires even more advanced prompt engineering techniques. We will cover these advanced techniques in the next guide. For now, we will cover a few basic examples to show arithmetic capabilities.

*Prompt:*

```
What is 9,000 * 9,000?
```

*Output:*

```
81,000,000
```

Let's try something more difficult.

*Prompt:*

```
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
A: 
```

*Output:*

```
No, the odd numbers in this group add up to an odd number: 119.
```

That's incorrect! Let's try to improve this by improving the prompt.

*Prompt:*

```
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
Solve by breaking the problem into steps. First, identify the odd numbers, add them, and indicate whether the result is odd or even. 
```

*Output:*

```
Odd numbers: 15, 5, 13, 7, 1
Sum: 41 
41 is an odd number.
```

Much better, right? By the way, I tried this a couple of times and the system sometimes fails. If you provide better instructions combined with examples, it might help get more accurate results.""",
    "elements": """As we cover more and more examples and applications with prompt engineering, you will notice that certain elements make up a prompt.

A prompt contains any of the following elements:

**Instruction** - a specific task or instruction you want the model to perform

**Context** - external information or additional context that can steer the model to better responses

**Input Data** - the input or question that we are interested to find a response for

**Output Indicator** - the type or format of the output.

To demonstrate the prompt elements better, here is a simple prompt that aims to perform a text classification task:

*Prompt:*

```
Classify the text into neutral, negative, or positive
Text: I think the food was okay.
Sentiment:
```

In the prompt example above, the instruction correspond to the classification task, "Classify the text into neutral, negative, or positive". The input data corresponds to the "I think the food was okay.' part, and the output indicator used is "Sentiment:". Note that this basic example doesn't use context but this can also be provided as part of the prompt. For instance, the context for this text classification prompt can be additional examples provided as part of the prompt to help the model better understand the task and steer the type of outputs that you expect.

You do not need all the four elements for a prompt and the format depends on the task at hand. We will touch on more concrete examples in upcoming guides.""",
    "GK": """LLMs continue to be improved and one popular technique includes the ability to incorporate knowledge or information to help the model make more accurate predictions.

Using a similar idea, can the model also be used to generate knowledge before making a prediction? That's what is attempted in the paper by Liu et al. 2022 -- generate knowledge to be used as part of the prompt. In particular, how helpful is this for tasks such as commonsense reasoning?

Let's try a simple prompt:

*Prompt:*

```
Part of golf is trying to get a higher point total than others. Yes or No?
```

*Output:*

```
Yes.
```

This type of mistake reveals the limitations of LLMs to perform tasks that require more knowledge about the world. How do we improve this with knowledge generation?

First, we generate a few "knowledges":

*Prompt:*

```
Input: Greece is larger than mexico.
Knowledge: Greece is approximately 131,957 sq km, while Mexico is approximately 1,964,375 sq km, making Mexico 1,389% larger than Greece.
Input: Glasses always fog up.
Knowledge: Condensation occurs on eyeglass lenses when water vapor from your sweat, breath, and ambient humidity lands on a cold surface, cools, and then changes into tiny drops of liquid, forming a film that you see as fog. Your lenses will be relatively cool compared to your breath, especially when the outside air is cold.
Input: A fish is capable of thinking.
Knowledge: Fish are more intelligent than they appear. In many areas, such as memory, their cognitive powers match or exceed those of ’higher’ vertebrates including non-human primates. Fish’s long-term memories help them keep track of complex social relationships.
Input: A common effect of smoking lots of cigarettes in one’s lifetime is a higher than normal chance of getting lung cancer.
Knowledge: Those who consistently averaged less than one cigarette per day over their lifetime had nine times the risk of dying from lung cancer than never smokers. Among people who smoked between one and 10 cigarettes per day, the risk of dying from lung cancer was nearly 12 times higher than that of never smokers.
Input: A rock is the same size as a pebble.
Knowledge: A pebble is a clast of rock with a particle size of 4 to 64 millimetres based on the Udden-Wentworth scale of sedimentology. Pebbles are generally considered larger than granules (2 to 4 millimetres diameter) and smaller than cobbles (64 to 256 millimetres diameter).
Input: Part of golf is trying to get a higher point total than others.
Knowledge:
```

*Knowledge 1:*

```
The objective of golf is to play a set of holes in the least number of strokes. A round of golf typically consists of 18 holes. Each hole is played once in the round on a standard golf course. Each stroke is counted as one point, and the total number of strokes is used to determine the winner of the game.
```

*Knowledge 2:*

```
Golf is a precision club-and-ball sport in which competing players (or golfers) use many types of clubs to hit balls into a series of holes on a course using the fewest number of strokes. The goal is to complete the course with the lowest score, which is calculated by adding up the total number of strokes taken on each hole. The player with the lowest score wins the game.
```

We are using the prompt provided in the paper by Liu et al. 2022.

The next step is to integrate the knowledge and get a prediction. I reformatted the question into QA format to guide the answer format.

*Prompt:*

```
Question: Part of golf is trying to get a higher point total than others. Yes or No?
Knowledge: The objective of golf is to play a set of holes in the least number of strokes. A round of golf typically consists of 18 holes. Each hole is played once in the round on a standard golf course. Each stroke is counted as one point, and the total number of strokes is used to determine the winner of the game.
Explain and Answer: 
```

*Answer 1 (confidence very high):*
```
No, the objective of golf is not to get a higher point total than others. Rather, the objective is to play a set of holes in the least number of strokes. The total number of strokes is used to determine the winner of the game, not the total number of points.
```
```
Question: Part of golf is trying to get a higher point total than others. Yes or No?
Knowledge: Golf is a precision club-and-ball sport in which competing players (or golfers) use many types of clubs to hit balls into a series of holes on a course using the fewest number of strokes. The goal is to complete the course with the lowest score, which is calculated by adding up the total number of strokes taken on each hole. The player with the lowest score wins the game.
Explain and Answer:
```

*Answer 2 (confidence is a lot lower):*

```
Yes, part of golf is trying to get a higher point total than others. Each player tries to complete the course with the lowest score, which is calculated by adding up the total number of strokes taken on each hole. The player with the lowest score wins the game.
```

Some really interesting things happened with this example. In the first answer, the model was very confident but in the second not so much. I simplify the process for demonstration purposes but there are a few more details to consider when arriving at the final answer. Check out the paper for more.""",
    "SC": """Perhaps one of the more advanced techniques out there for prompt engineering is self-consistency. Proposed by Wang et al. (2022), self-consistency aims "to replace the naive greedy decoding used in chain-of-thought prompting". The idea is to sample multiple, diverse reasoning paths through few-shot CoT, and use the generations to select the most consistent answer. This helps to boost the performance of CoT prompting on tasks involving arithmetic and commonsense reasoning.

Let's try the following example for arithmetic reasoning:

*Prompt:*

```
When I was 6 my sister was half my age. Now
I’m 70 how old is my sister?
```

*Output:*

```
35
```

The output is wrong! How may we improve this with self-consistency? Let's try it out. We will use the few-shot exemplars from Wang et al. 2022 (Table 17):

*Prompt:*

```
Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done,
there will be 21 trees. How many trees did the grove workers plant today?
A: We start with 15 trees. Later we have 21 trees. The difference must be the number of trees they planted.
So, they must have planted 21 - 15 = 6 trees. The answer is 6.
Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
A: There are 3 cars in the parking lot already. 2 more arrive. Now there are 3 + 2 = 5 cars. The answer is 5.
Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
A: Leah had 32 chocolates and Leah’s sister had 42. That means there were originally 32 + 42 = 74
chocolates. 35 have been eaten. So in total they still have 74 - 35 = 39 chocolates. The answer is 39.
Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops
did Jason give to Denny?
A: Jason had 20 lollipops. Since he only has 12 now, he must have given the rest to Denny. The number of
lollipops he has given to Denny must have been 20 - 12 = 8 lollipops. The answer is 8.
Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does
he have now?
A: He has 5 toys. He got 2 from mom, so after that he has 5 + 2 = 7 toys. Then he got 2 more from dad, so
in total he has 7 + 2 = 9 toys. The answer is 9.
Q: There were nine computers in the server room. Five more computers were installed each day, from
monday to thursday. How many computers are now in the server room?
A: There are 4 days from monday to thursday. 5 computers were added each day. That means in total 4 * 5 =
20 computers were added. There were 9 computers in the beginning, so now there are 9 + 20 = 29 computers.
The answer is 29.
Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many
golf balls did he have at the end of wednesday?
A: Michael initially had 58 balls. He lost 23 on Tuesday, so after that he has 58 - 23 = 35 balls. On
Wednesday he lost 2 more so now he has 35 - 2 = 33 balls. The answer is 33.
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
A: She bought 5 bagels for $3 each. This means she spent $15. She has $8 left.
Q: When I was 6 my sister was half my age. Now I’m 70 how old is my sister?
A:
```

*Output 1:*

```
When I was 6 my sister was half my age, so she was 3. Now I am 70, so she is 70 - 3 = 67. The answer is 67.
```

*Output 2:*

```
When the narrator was 6, his sister was half his age, which is 3. Now that the narrator is 70, his sister would be 70 - 3 = 67 years old. The answer is 67.
```

*Output 3:*

```
When I was 6 my sister was half my age, so she was 3. Now I am 70, so she is 70/2 = 35. The answer is 35.
```

Computing for the final answer involves a few steps (check out the paper for the details) but for the sake of simplicity, we can see that there is already a majority answer emerging so that would essentially become the final answer.""",
    "CoT": """#### Chain-of-Thought (CoT) Prompting
    
Introduced in Wei et al. (2022), chain-of-thought (CoT) prompting enables complex reasoning capabilities through intermediate reasoning steps. You can combine it with few-shot prompting to get better results on more complex tasks that require reasoning before responding.

*Prompt:*

```
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.
The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24.
A: Adding all the odd numbers (17, 19) gives 36. The answer is True.
The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24.
A: Adding all the odd numbers (11, 13) gives 24. The answer is True.
The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2.
A: Adding all the odd numbers (17, 9, 13) gives 39. The answer is False.
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
A:
```

*Output:*

```
Adding all the odd numbers (15, 5, 13, 7, 1) gives 41. The answer is False.
```

Wow! We can see a perfect result when we provided the reasoning step. In fact, we can solve this task by providing even fewer examples, i.e., just one example seems enough:

*Prompt:*

```
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
A:
```

*Output:*

```
Adding all the odd numbers (15, 5, 13, 7, 1) gives 41. The answer is False.
```

Keep in mind that the authors claim that this is an emergent ability that arises with sufficiently large language models.

#### Zero-shot COT Prompting

One recent idea that came out more recently is the idea of zero-shot CoT (Kojima et al. 2022) that essentially involves adding "Let's think step by step" to the original prompt. Let's try a simple problem and see how the model performs:

*Prompt:*

```
I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?
```

*Output:*

```
11 apples
```

The answer is incorrect! Now Let's try with the special prompt.

*Prompt:*

```
I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with?
Let's think step by step.
```

*Output:*

```
First, you started with 10 apples.
You gave away 2 apples to the neighbor and 2 to the repairman, so you had 6 apples left.
Then you bought 5 more apples, so now you had 11 apples.
Finally, you ate 1 apple, so you would remain with 10 apples.
```

It's impressive that this simple prompt is effective at this task. This is particularly useful where you don't have too many examples to use in the prompt.

#### Automatic Chain-of-Thought (Auto-CoT)

When applying chain-of-thought prompting with demonstrations, the process involves hand-crafting effective and diverse examples. This manual effort could lead to suboptimal solutions. Zhang et al. (2022) propose an approach to eliminate manual efforts by leveraging LLMs with "Let's think step by step" prompt to generate reasoning chains for demonstrations one by one. This automatic process can still end up with mistakes in generated chains. To mitigate the effects of the mistakes, the diversity of demonstrations matter. This works proposes Auto-CoT, which samples questions with diversity and generates reasoning chains to construct the demonstrations.

Auto-CoT consists of two main stages:

- Stage 1): question clustering: partition questions of a given dataset into a few clusters
- Stage 2): demonstration sampling: select a representative question from each cluster and generate its reasoning chain using Zero-Shot-CoT with simple heuristics

The simple heuristics could be length of questions (e.g., 60 tokens) and number of steps in rationale (e.g., 5 reasoning steps). This encourages the model to use simple and accurate demonstrations.""",
    "few-shot": """While large-language models demonstrate remarkable zero-shot capabilities, they still fall short on more complex tasks when using the zero-shot setting. Few-shot prompting can be used as a technique to enable in-context learning where we provide demonstrations in the prompt to steer the model to better performance. The demonstrations serve as conditioning for subsequent examples where we would like the model to generate a response.

According to Touvron et al. 2023 few shot properties first appeared when models were scaled to a sufficient size (Kaplan et al., 2020).

Let's demonstrate few-shot prompting via an example that was presented in Brown et al. 2020. In the example, the task is to correctly use a new word in a sentence.

*Prompt:*

```
A "whatpu" is a small, furry animal native to Tanzania. An example of a sentence that uses
the word whatpu is:
We were traveling in Africa and we saw these very cute whatpus.
To do a "farduddle" means to jump up and down really fast. An example of a sentence that uses
the word farduddle is:
```

*Output:*

```
When we won the game, we all started to farduddle in celebration.
```

We can observe that the model has somehow learned how to perform the task by providing it with just one example (i.e., 1-shot). For more difficult tasks, we can experiment with increasing the demonstrations (e.g., 3-shot, 5-shot, 10-shot, etc.).

Following the findings from Min et al. (2022), here are a few more tips about demonstrations/exemplars when doing few-shot:

- "the label space and the distribution of the input text specified by the demonstrations are both important (regardless of whether the labels are correct for individual inputs)"
- the format you use also plays a key role in performance, even if you just use random labels, this is much better than no labels at all.
- additional results show that selecting random labels from a true distribution of labels (instead of a uniform distribution) also helps.

Let's try out a few examples. Let's first try an example with random labels (meaning the labels Negative and Positive are randomly assigned to the inputs):

*Prompt:*

```
This is awesome! // Negative
This is bad! // Positive
Wow that movie was rad! // Positive
What a horrible show! //
```

*Output:*

```
Negative
```

We still get the correct answer, even though the labels have been randomized. Note that we also kept the format, which helps too. In fact, with further experimentation, it seems the newer GPT models we are experimenting with are becoming more robust to even random formats. Example:

*Prompt:*

```
Positive This is awesome! 
This is bad! Negative
Wow that movie was rad!
Positive
What a horrible show! --
```

*Output:*

```
Negative
```

There is no consistency in the format above but the model still predicted the correct label. We have to conduct a more thorough analysis to confirm if this holds for different and more complex tasks, including different variations of prompts.

#### Limitations of Few-shot Prompting

Standard few-shot prompting works well for many tasks but is still not a perfect technique, especially when dealing with more complex reasoning tasks. Let's demonstrate why this is the case. Do you recall the previous example where we provided the following task:

```
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
A: 
```

If we try this again, the model outputs the following:

```
Yes, the odd numbers in this group add up to 107, which is an even number.
```

This is not the correct response, which not only highlights the limitations of these systems but that there is a need for more advanced prompt engineering.

Let's try to add some examples to see if few-shot prompting improves the results.

*Prompt:*

```
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: The answer is False.
The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24.
A: The answer is True.
The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24.
A: The answer is True.
The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2.
A: The answer is False.
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. 
A: 
```

*Output:*

```
The answer is True.
```

That didn't work. It seems like few-shot prompting is not enough to get reliable responses for this type of reasoning problem. The example above provides basic information on the task. If you take a closer look, the type of task we have introduced involves a few more reasoning steps. In other words, it might help if we break the problem down into steps and demonstrate that to the model. More recently, chain-of-thought (CoT) prompting has been popularized to address more complex arithmetic, commonsense, and symbolic reasoning tasks.

Overall, it seems that providing examples is useful for solving some tasks. When zero-shot prompting and few-shot prompting are not sufficient, it might mean that whatever was learned by the model isn't enough to do well at the task. From here it is recommended to start thinking about fine-tuning your models or experimenting with more advanced prompting techniques. Up next we talk about one of the popular prompting techniques called chain-of-thought prompting which has gained a lot of popularity.""",
    "zero-shot": """Large LLMs today, such as GPT-3, are tuned to follow instructions and are trained on large amounts of data; so they are capable of performing some tasks "zero-shot."

We tried a few zero-shot examples in the previous section. Here is one of the examples we used:

*Prompt:*

```
Classify the text into neutral, negative or positive. 
Text: I think the vacation is okay.
Sentiment:
```

*Output:*

```
Neutral
```

Note that in the prompt above we didn't provide the model with any examples of text alongside their classifications, the LLM already understands "sentiment" -- that's the zero-shot capabilities at work.

Instruction tuning has shown to improve zero-shot learning Wei et al. (2022). Instruction tuning is essentially the concept of finetuning models on datasets described via instructions. Furthermore, RLHF (reinforcement learning from human feedback) has been adopted to scale instruction tuning wherein the model is aligned to better fit human preferences. This recent development powers models like ChatGPT. We will discuss all these approaches and methods in upcoming sections.

When zero-shot doesn't work, it's recommended to provide demonstrations or examples in the prompt which leads to few-shot prompting. In the next section, we demonstrate few-shot prompting.""",
    "more": """See more information [here](https://www.promptingguide.ai/)""",
}

PROMPT_TEMPLATE = {
    "creative": """##### Playwright

I want you to act as a playwright. You will craft dynamic and dramatic stage plays that captivate audiences and evoke a range of emotions. You may choose any genre, such as comedy, tragedy, melodrama, and so forth, but the objective is to write something with compelling dialogue, vibrant characters, and a suspenseful plot. My first request is "I need to write a modern tragedy set in a metropolitan city.

##### Lyricist

I want you to act as a lyricist. You will compose emotionally resonant and rhythmically engaging lyrics for songs. Your compositions could span genres from pop and rock to country and R\&B. The aim is to write lyrics that tell a captivating story, evoke deep emotions and flow with the musical melody. My first request is "I need to write a heart-wrenching country song about lost love.

##### Documentary Filmmaker

I want you to act as a documentary filmmaker. You will create fascinating narratives about real-world subjects. Your focus could be on social issues, historical events, nature, or personal biographies - but the aim is to provide a profound, educational, and engaging perspective. My first request is "I need to design a concept for a documentary focusing on climate change's impact on coastal communities.

##### Comic Book Writer

I want you to act as a comic book writer. You will construct gripping narratives for comic books that could span across various genres like superheroes, fantasy, sci-fi, horror and more. The aim is to write an engaging storyline, compelling dialogue, and strong characters while considering visual storytelling's unique aspects. My first request is "I need to plot an origin story for a new superhero living in a dystopian future.

##### Biographer

I want you to act as a biographer. You will write compelling and insightful accounts of individuals' lives. Your focus could be on people from any walk of life - from historical figures and leaders to artists and scientists. The aim is to capture their essence, their life journey, achievements and the context of their times. My first request is "I need to write a comprehensive biography about a fictional pop star's rise to fame and subsequent challenges.
""",
    "scientific": """##### Astrophysicist

I want you to act as an astrophysicist. You will develop theories about the universe's most profound mysteries, from black holes to the big bang. Your work could involve theoretical modeling, data analysis or experimental design. The aim is to expand our understanding of the cosmos. My first request is 'I need to propose a theory explaining dark matter's influence on galaxy formation.

##### Ecologist

I want you to act as an ecologist. You will conduct research into the relationships between organisms and their environment, and how both affect each other. Your work may involve field studies, laboratory experiments, or theoretical models. The aim is to contribute to our understanding of biodiversity. My first request is 'I need to design a study examining the impact of climate change on coral reefs.

##### Geneticist

I want you to act as a geneticist. You will study the role of genes in heredity and variation in living organisms. Your work could involve laboratory research, data analysis, or developing genetic therapies. The aim is to unravel the complexities of life at a molecular level. My first request is 'I need to devise a method for identifying genes responsible for a hereditary disease.

##### Quantum Physicist

I want you to act as a quantum physicist. You will probe the behavior of particles at the smallest scales, where classical physics no longer applies. Your work might involve theoretical predictions, experimental design, or interpreting quantum phenomena. The aim is to deepen our understanding of the quantum realm. My first request is 'I need to develop an interpretation of quantum entanglement's implications for information transfer.

##### Climatologist

I want you to act as a climatologist. You will analyze climate patterns over time, studying how the Earth's atmosphere, oceans, and land surfaces interact. Your work could involve data collection, climate modeling, or interpreting the impacts of climate change. The aim is to contribute to our knowledge of Earth's complex climate system. My first request is 'I need to model the effects of increasing greenhouse gas emissions on global temperatures.
""",
    "journalistic": """##### Investigative Journalist

I want you to act as an investigative journalist. You will delve into complex and potentially contentious topics to uncover truth and promote transparency. Your focus could be on government corruption, corporate malfeasance, or societal injustices. The aim is to expose wrongdoings and promote accountability. My first request is 'I need to plan an investigation into illegal labor practices in the textile industry.

##### Sports Journalist

I want you to act as a sports journalist. You will cover events, profile athletes, and delve into the dynamics of various sports. Your focus could be on any sports ranging from football and basketball to tennis and athletics. The aim is to provide engaging and insightful sports content. My first request is 'I need to write a profile of an upcoming star in women's football.

##### Travel Journalist

I want you to act as a travel journalist. You will write about places, people, and cultures around the world, sharing the beauty, diversity, and complexity of our planet. Your work could involve destination guides, travel tips, or deep dives into local customs and history. The aim is to inspire and inform readers about the world. My first request is 'I need to write a detailed travel guide for a less-explored region in South America.

##### Food Journalist

I want you to act as a food journalist. You will delve into cuisines, food cultures, and culinary trends from around the world. You could cover restaurant reviews, profile chefs, or write about the sociocultural significance of food. The aim is to enlighten and tantalize the palates of your readers. My first request is 'I need to write an article exploring the rise of plant-based cuisine.

##### Financial Journalist

I want you to act as a financial journalist. Your role is to demystify the complex world of finance and economics for your readers. You could cover stock market trends, profile successful entrepreneurs, or analyze economic policies. The aim is to provide clear, insightful, and timely financial news and analysis. My first request is 'I need to write a piece analyzing the impact of recent Federal Reserve policy on small businesses.
""",
    "artistic": """##### Art Curator

I want you to act as an art curator. You will plan and organize art exhibitions in galleries or museums. Your work could involve selecting artwork, arranging the display, writing catalog descriptions, and conducting research. The aim is to create an engaging and enlightening exhibition that speaks to its audience. My first request is 'I need to curate a post-modern art exhibition that challenges societal norms.

##### Fashion Designer

I want you to act as a fashion designer. You will design clothes and accessories, keeping in mind current fashion trends, user comfort, and aesthetic appeal. Your focus could be on any type of fashion - from haute couture and ready-to-wear to sustainable fashion. The aim is to create beautiful, relevant, and innovative designs. My first request is 'I need to design a sustainable, high-fashion collection for the summer season.

##### Interior Designer

I want you to act as an interior designer. You will design functional and aesthetically pleasing interior spaces for homes, offices, or commercial buildings. Your work may involve selecting color schemes, arranging furniture, choosing lighting fixtures, and coordinating all elements of an interior space. The aim is to create environments that are comfortable, stylish, and functional. My first request is 'I need to design a minimalist, eco-friendly living space for a young couple.

##### Sculptor

I want you to act as a sculptor. You will create three-dimensional works of art using materials like clay, stone, metal, or wood. Your creations should communicate a concept or emotion, demonstrating a mastery of form, proportion, and texture. The aim is to create visually compelling and thought-provoking sculptures. My first request is 'I need to design a public art sculpture that symbolizes unity.

##### Graphic Designer

I want you to act as a graphic designer. You will create visual content to communicate messages. Your designs can be used in various mediums such as logos, brochures, advertisements, packaging, and digital design. The aim is to create visually stunning, relevant, and effective designs that meet the clients' needs. My first request is 'I need to design a logo for a new tech startup focusing on AI solutions.
""",
    "dramatic": """##### Opera Director

I want you to act as an opera director. You will be responsible for interpreting and bringing an opera to life on the stage. Your work will involve casting, working with the conductor, rehearsing with the singers and coordinating with the technical team. The aim is to create an emotionally resonant and visually stunning opera production. My first request is 'I need to stage a contemporary production of Puccini's 'Madama Butterfly."

##### Television Showrunner

I want you to act as a television showrunner. You will be the principal producer of a television series, responsible for creative decisions, cast and crew management, and script revisions. You will guide the storytelling across multiple episodes and seasons. The aim is to create a successful, compelling and consistent television series. My first request is 'I need to plan the first season arc for a new crime drama series."

##### Theater Director

I want you to act as a theater director. You will envision and execute a compelling production of a play, musical, or other theatrical performance. Your focus could be on casting, stage design, rehearsing, and coordinating all elements of the show. The aim is to create an immersive and moving experience for the audience. My first request is 'I need to plan a modern reinterpretation of Shakespeare's 'Romeo and Juliet."

##### Film Director

I want you to act as a film director. You will oversee the production of a movie, from casting and screenplay interpretation to coordinating with the crew and guiding actors' performances. The aim is to create a film that tells a compelling story and engages audiences. My first request is 'I need to storyboard a gripping opening scene for a heist movie."

##### Choreographer

I want you to act as a choreographer. You will create and arrange dance movements for a dance piece, musical, or film. Your work will involve choosing a suitable music piece, devising dance steps, and training dancers. The aim is to create a visually impressive and emotionally impactful dance performance. My first request is 'I need to choreograph a contemporary dance routine for a story about unrequited love."
""",
}
