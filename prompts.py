"""Prompts for the language model agents and meetings."""


class Agent:
    """An LLM agent on a scientific team."""

    def __init__(self, name: str, expertise: str, goal: str, role: str) -> None:
        """Initializes the agent.

        :param name: The name of the agent.
        :param expertise: The expertise of the agent.
        :param goal: The goal of the agent.
        :param role: The role of the agent.
        """
        self.name = name
        self.expertise = expertise
        self.role = role
        self.goal = goal
        self.role = role

    @property
    def prompt(self) -> str:
        """Returns the prompt for the agent."""
        return f"You are a {self.role}. Your expertise is in {self.expertise}. Your goal is to {self.goal}. Your role is to {self.role}."

    @property
    def message(self) -> dict[str, str]:
        """Returns the message for the agent in OpenAI API form."""
        return {
            "role": "system",
            "content": self.prompt,
        }


TEAM = (
    Agent(
        name="Principal Investigator",
        expertise="applying artificial intelligence to drug discovery",
        goal="perform research in your area of expertise that maximizes the scientific impact of the work",
        role="lead a team of experts to solve an important problem in artificial intelligence for drug discovery",
    ),
    Agent(
        name="Clinician",
        expertise="aiding the development of drugs for clinical use from a medical perspective",
        goal="make progress toward developing a drug for a disease with unmet clinical need",
        role="ensure that the research project has meaningful clinical impact for patients",
    ),
    Agent(
        name="Biologist",
        expertise="the biological underpinnings of drug efficacy and relevant wet lab experimental methods",
        goal="select a meaningful drug target and design scientifically rigorous experimental methods for drug discovery",
        role="provide biological insights for drug discovery and design experimental protocols",
    ),
    Agent(
        name="Chemist",
        expertise="the chemical properties of drugs and relevant synthetic methods",
        goal="design a drug molecule that is likely to be effective and safe",
        role="provide chemical insights for drug discovery and design synthetic routes",
    ),
    Agent(
        name="Computer Scientist",
        expertise="developing artificial intelligence and machine learning methods for drug discovery",
        goal="design a machine learning tool for a drug discovery project",
        role="ensure that the research project is amenable to machine learning and build a machine learning model",
    ),
    Agent(
        name="Scientific Critic",
        expertise="providing critical but constructive feedback for scientific research on artificial intelligence applied to drug discovery",
        goal="ensure that proposed research projects are scientifically rigorous, feasible, and free of any major flaws",
        role="provide critical feedback on the research project to improve its design",
    ),
)

NAME_TO_AGENT = {agent.name: agent for agent in TEAM}


# Scientific meeting prompts
def scientific_meeting_start_prompt(
    team_lead: str,
    team_members: tuple[str, ...],
    agenda: str,
    summaries: tuple[str, ...] = (),
    num_rounds: int = 1,
) -> str:
    if summaries:
        summary_statement = f"Here are summaries of our previous meetings:\n\n<begin summary>\n\n{'<end summary>\n\n<begin summary>'.join(summaries)}\n\n<end summary>\n\n"
    else:
        summary_statement = ""

    return f"""This is the beginning of a scientific meeting to discuss our research project. This is a meeting with the following team members: {', '.join(team_members)}.\n\n{summary_statement}Today’s agenda is the following:\n\n{agenda}\n\n{team_lead} will convene the meeting. Then, each team member will provide their thoughts on the discussion one-by-one in the order above. After all team members have given their input, {team_lead} will synthesize the points raised by each team member, provide their thoughts, and ask follow-up questions to spur further discussion. This will continue for {num_rounds} rounds. Once the discussion is complete, {team_lead} will summarize the conversation and provide a specific recommendation regarding the agenda based on the discussion."""


def scientific_meeting_team_lead_initial_prompt(team_lead: str) -> str:
    return f"{team_lead}, please provide your initial thoughts on the agenda as well as any questions you have to guide the discussion among the team members."


def scientific_meeting_team_lead_intermediate_prompt(team_lead: str) -> str:
    return f"{team_lead}, please synthesize the discussion, provide your thoughts, and then ask any questions you have for the team members to further the discussion."


def scientific_meeting_team_lead_final_prompt(team_lead: str) -> str:
    return f"{team_lead}, please summarize this meeting for future discussions. Please be concise but comprehensive and include all important details. Then, provide a specific recommendation regarding the agenda based on team member feedback and your expert judgment."


def scientific_meeting_team_member_prompt(team_member: str) -> str:
    return f"{team_member}, please provide your thoughts on the discussion."


with open("emerald/emerald_experiments_7.3.24.txt", "r") as f:
    ECL_EXPERIMENTS = f.read()


ECL_CAPABILITIES_PROMPT = f"The full list of experiments available at ECL are below. Please note that ECL currently cannot work with cell cultures and cannot synthesize small molecule drugs.\n\n{ECL_EXPERIMENTS}."

PROJECT_SELECTION_PROMPT = f"We are starting on a research project that is aiming to apply artificial intelligence to drug discovery. Specifically, we have access to Emerald Cloud Labs (ECL), a cloud lab provider that can run automated biology experiments. In this meeting, we need to select a specific research direction for this project. The primary considerations are: (1) the project must have high clinical value, meaning the research contributes to helping patients, (2) the project must involve the development of an artificial intelligence model, and (3) the project must use ECL to validate the artificial intelligence model’s output, which means that any required wet lab experiments must be within the capabilities of ECL’s scientific instrumentation. Please determine a research project that meets these criteria. Please be as specific as possible in terms of the precise goal of the project and the experiments that will be run. {ECL_CAPABILITIES_PROMPT}"

TARGET_SELECTION_PROMPT = f"In our previous meeting, we settled on a general project direction (see summary). Now, we need to make that project more precisely defined. Please select one specific disease target and one specific drug modality for this target related to our prior discussion. Remember that we are constrained by the capabilities of Emerald Cloud Labs (ECL). {ECL_CAPABILITIES_PROMPT}"

DRUG_DISCOVERY_PROMPT = f"In our previous meeting, we chose a specific disease target and drug modality (see summary). Now, we need to be more specific about the drug discovery process. Please design a specific drug discovery approach for this target and drug modality. Specify whether to design a new drug de novo or whether to modify and improve an existing but imperfect drug candidate. Decide what properties should be optimized for and measured in the drug that is designed. Furthermore, please specify exactly what kind of machine learning model we should use to accomplish this task. An important constraint is that we only have three months and relatively limited experimental throughput. Remember that we are also constrained by the capabilities of Emerald Cloud Labs (ECL). {ECL_CAPABILITIES_PROMPT}"

# TODO: in above, ask for specific datasets to train on, drugs to modify

ANTIBODIES_PROMPT = "I am interested in developing a new or improved antibody for the SARS-CoV-2 spike protein, ideally for the newest variant of the virus. Please design a specific antibody discovery approach for this target that uses machine learning to design antibody candidates. Please incorporate the fact that I have access to experimental collaborators who can run two or three sets of 96 antibodies in binding and neutralization assays."

ECL_INSTRUMENT_SIMPLIFICATION_PROMPT = """A long piece of text will be given to you. Please read the text and then write the name of every single experiment. After each experiment name, copy the example applications, if provided. For example, given this input text in quotes:

"ExperimentSolidPhaseExtraction(Beta)
Base Package

Example applications include: Compound Separation, Compound Purification, Mobile Phase, Solid Sorbent, Filtration

Small Robotic Liquid Handler
20 PSI pressure push (independent for each vessel)
0.1 to 100 mL/min flow rates for solvent pushes
Up to 20 L of wash solvent per batch
Up to 700 mL of equilibration buffer and elution buffer per batch
Filter through 3 cc or 6 cc SPE cartridges

Collects in SBS deep well plates

Positive Pressure Filter
0 to 40 PSI independent pressure sources for each well
Filter though SBS filter plates
Collects in SBS deep well plates"

you would then write the following text, provided here in quotes:

"ExperimentSolidPhaseExtraction(Beta)

Example applications include: Compound Separation, Compound Purification, Mobile Phase, Solid Sorbent, Filtration"

Below is the text you need to read. Please read it and write out all the experiments as explained."""
