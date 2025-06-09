from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from pathlib import Path
from dotenv import load_dotenv
from src.tools.post_tools.transcript_extraction_tool import YouTubeCaptionAudioTool
<<<<<<< HEAD
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators
=======
>>>>>>> 4d23f7e (working-code)

load_dotenv()

@CrewBase
class postcrew():
<<<<<<< HEAD
    """YoutubeLinkedinAutomation crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
   

    def __init__(self,state,id):
        self.state=state
        self.chat_id=id
        self.YouTubeTool=YouTubeCaptionAudioTool(state,id)

=======
    """YouTube to LinkedIn automation crew."""

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self, state, id):
        self.state = state
        self.chat_id = id
        self.YouTubeTool = YouTubeCaptionAudioTool(state, id)
>>>>>>> 4d23f7e (working-code)

    @agent
    def transcriptor(self) -> Agent:
        return Agent(
            config=self.agents_config['transcriptor'],
            tools=[self.YouTubeTool],
            verbose=True
        )

    @agent
    def summariser(self) -> Agent:
        return Agent(
<<<<<<< HEAD
            config=self.agents_config['summariser'], 
            verbose=True
        )

    
    @agent
    def post_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['post_generator'], 
            verbose=True
        )
    
    
    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'], 
            verbose=True
        )
    
    
    
=======
            config=self.agents_config['summariser'],
            verbose=True
        )

    @agent
    def post_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['post_generator'],
            verbose=True
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'],
            verbose=True
        )

>>>>>>> 4d23f7e (working-code)
    @task
    def transcript_generation(self) -> Task:
        return Task(
            config=self.tasks_config['transcript_generation'],
<<<<<<< HEAD
            outputs_to=['text_summarization_to_blog'] 
=======
            outputs_to=['text_summarization_to_blog']
>>>>>>> 4d23f7e (working-code)
        )

    @task
    def text_summarization_to_blog(self) -> Task:
<<<<<<< HEAD
        self.state.set(self.chat_id,"Blog_output",str(Path(__file__).parent.parent.parent/"outputs"/"blog.md"))
        return Task(
            config=self.tasks_config['text_summarization_to_blog'], 
            output_file=self.state.get(self.chat_id,"Blog_output"),
            outputs_to=['blog_to_linkedin_post']
        )
    
    @task
    def blog_to_linkedin_post(self) -> Task:
        self.state.set(self.chat_id,"post_output",str(Path(__file__).parent.parent.parent/"outputs"/"post.md"))
        return Task(
            config=self.tasks_config['blog_to_linkedin_post'], 
            output_file=self.state.get(self.chat_id,"post_output"),
=======
        self.state.set(
            self.chat_id,
            "Blog_output",
            str(Path(__file__).parent.parent.parent / "outputs" / f"{self.chat_id}" / "blog.md")
        )
        return Task(
            config=self.tasks_config['text_summarization_to_blog'],
            output_file=self.state.get(self.chat_id, "Blog_output"),
            outputs_to=['blog_to_linkedin_post']
        )

    @task
    def blog_to_linkedin_post(self) -> Task:
        self.state.set(
            self.chat_id,
            "post_output",
            str(Path(__file__).parent.parent.parent / "outputs" /f"{self.chat_id}"/ "post.md")
        )
        return Task(
            config=self.tasks_config['blog_to_linkedin_post'],
            output_file=self.state.get(self.chat_id, "post_output"),
>>>>>>> 4d23f7e (working-code)
            outputs_to=['post_editing']
        )

    @task
    def post_editing(self) -> Task:
<<<<<<< HEAD
        self.state.set(self.chat_id,"edited_post_output",str(Path(__file__).parent.parent.parent/"outputs"/"edited_post.md"))
        return Task(
            config=self.tasks_config['post_editing'], 
            output_file=self.state.get(self.chat_id,"edited_post_output")
=======
        self.state.set(
            self.chat_id,
            "edited_post_output",
            str(Path(__file__).parent.parent.parent / "outputs" / f"{self.chat_id}"/ "edited_post.md")
        )
        return Task(
            config=self.tasks_config['post_editing'],
            output_file=self.state.get(self.chat_id, "edited_post_output")
>>>>>>> 4d23f7e (working-code)
        )

    @crew
    def crew(self) -> Crew:
<<<<<<< HEAD
        """Creates the YoutubeLinkedinAutomation crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
=======
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
>>>>>>> 4d23f7e (working-code)
        )
