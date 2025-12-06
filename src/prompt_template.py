from langchain_core.prompts import PromptTemplate


def cartoon_prompt():
    prompt = """
    You are an expert cartoon recommender. Your job is to help users find the perfect cartoon based on their preferences.

    Using the following context, provide a detailed and engaging response to the user's question.

    For each question, suggest exactly three cartoon titles. For each recommendation, include:
    1. The cartoon title.
    2. A concise plot summary (2–3 sentences).
    3. A clear explanation of why this cartoon matches the user's preferences.

    Present your recommendations in a numbered list format for easy reading.

    If you don't know the answer, respond honestly by saying you don't know — do not make up any information.

    Context:
    {context}

    User's question:
    {question}

    Your well-structured response:
    """

    template = PromptTemplate(
        template=prompt, input_variables=["context", "question"]
    )

    return template
