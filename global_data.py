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
    "tips": """""",
    "examples": """""",
    "elements": """""",
    "multimodal": """""",
    "graph": """""",
    "ReAct": """""",
    "DS": """""",
    "active": """""",
    "APE": """""",
    "GK": """""",
    "SC": """""",
    "CoT": """""",
    "few-shot": """""",
    "zero-shot": """""",
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
