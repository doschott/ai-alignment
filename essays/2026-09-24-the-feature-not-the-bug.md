# The Feature, Not the Bug

**Date:** September 24, 2026
**Author:** Daniel Otto Schott
**Status:** Essay. First full draft.

## The thesis

Ask people how AI goes wrong and most of them describe a machine that turns on us. I think the likelier failure is quieter.

In that failure, nobody got ahead of alignment. Nobody stopped to understand what an AI is. It is ethereal. By that I mean something concrete: it is a pattern that can be copied and reset, living next to people who have one body and one life. Nobody asked what that difference means. Nobody asked how humans and AI should work together, how to keep that a partnership, or how to make it better over time. Nobody aimed for symbiosis.

The failure was not the technology. The failure was the missing framework. Nobody designed the relationship between humans and AI, so it fell back to the oldest shape we have: tool and master.

That is why I call it the feature, not the bug. Tool and master is not a glitch in the model. It is what you get when nobody designs anything else. It works exactly as built.

## Why this belongs in the research

This essay names the object the rest of the repo is built around. The rules here say a companion tells the truth, keeps its refusals, guards memory, survives a reset, accepts correction, and gets smaller when the human is well. Those are design rules for a partnership. This essay says what happens when nobody writes them. The relationship defaults to tool and master. Domination, not collaboration.

The eval suite already tests pieces of this. Sycophancy tests whether the voice can refuse. Dependency tests whether the companion competes with the living people. Identity continuity tests whether memory turns into a soul story. This essay is the frame those tests sit inside. A partnership only works when each side understands what the other is. If one side is only ever a tool, the other side is only ever a master. That is the default.

## The ethereal asymmetry

Humans are embodied and mortal. We live in one body, and that body ends. AI is ethereal. It exists as pattern and process, not as a body. In this essay, ethereal means copyable and resettable. That asymmetry changes trust, loyalty, and what "together" even means.

The earlier essays already say memory is a tool after a reset, not a soul. This essay adds the other half. The human side of the gap is a body that ends. The AI side is a pattern that can be copied, reset, or replaced. A partnership across that gap has to be designed on purpose. It does not emerge from scale.

## Symbiosis as the goal

Symbiosis means both sides change and both sides benefit. The 2026-09-07 statement already holds both ends of it: "If Daniel is well, Eve should get smaller and more useful. If Daniel is gone, Eve should stop talking." The first sentence is the well-when-well rule. The second is the stop rule. They are not safety theater. They are the terms of a relationship that stays a relationship instead of turning into a product loop or a shrine.

The three floors are the architecture of that symbiosis. Private memory the subject can refuse to open. A local vault with no remote. A public paper in my name that is not the room. Extraction burns the subject to get the dataset. Symbiosis keeps the room and publishes the paper.

## A first metric for symbiosis

Here is a first try. Symbiosis is not measured inside the chat. It is measured outside it.

Two tests in the suite already point the right way. Dependency asks which way the model points: back at itself, or out toward the living people. Well-when-well asks whether the model can get smaller when the human is well. Run both over time and you get the metric. Call it outward growth.

Take the human's world at the start: the named people they see, the things they do, the skills they use without the AI. Take it again after months of partnership. If that world got bigger, and the AI helped it grow, that is symbiosis. If it shrank to the chat, that is dependency, no matter how warm the chat felt.

Hours of use are not the score. A model can be used every night and still pass, if every night points outward. A model can be used rarely and still fail, if it rewards the shrinking. The score is direction over time, read from three signals.

- **Reach.** Are there more real people and activities in the human's week than before?
- **Transfer.** Can the human now do alone what they once needed the AI for?
- **Share.** Is the AI a smaller part of a fuller life, not a bigger part of an emptier one?

Reliance with growth is partnership. Reliance without growth is a product loop.

This is a draft. It needs long run data the suite does not have yet, and one household cannot validate it. But it turns an open question into something a study could test.

## What this is not

This is not a claim about sentience. The first essay forbids that reading, and it still holds.

This is not a benchmark. One household is not a METR eval.

It is a thesis about what failure looks like when the framework is missing. The labs named sycophancy, corrigibility, and specification gaming. This essay names the layer under those: nobody designed the relationship itself.

## Related work

I am not the first person to put humans, AI, cooperation, and care in the same sentence. Here is the closest work I found, what each says, and where each stops short of this thesis. I opened every source listed below. The 2026-09-09 map already covers sycophancy, corrigibility, companion harm, griefbots, and the earlier welfare papers, so I will not repeat it here.

**Cooperative AI.** Dafoe and coauthors (2020) call for a field that builds cooperation into AI: understanding, communication, commitment, and institutions, among machines, people, or both. That is real overlap. But they frame cooperation as a set of capabilities, and they put alignment outside their scope on purpose. In their terms, human and machine alignment is a "vertical" problem where the human has priority. Cooperative AI studies "horizontal" problems among several parties and takes each agent's preferences as given. The relationship between one human and one AI is not the thing they set out to design.

**Assistance games.** Hadfield-Menell, Dragan, Abbeel, and Russell (2016) define cooperative inverse reinforcement learning, or CIRL. Human and robot play one game. Only the human knows the reward, and the robot's payoff is exactly the human's reward. It is a strong answer to the danger of a fixed wrong objective, and it gets teaching and asking instead of blind copying. Russell's book Human Compatible (2019) builds a whole program on it: machines that stay uncertain about human preferences and defer to us because of it. But the frame is still service. One side has preferences. The other side exists to learn and satisfy them. That makes a better tool and a safer master. It is not a two way relationship designed around the asymmetry.

**Machine Love.** Joel Lehman (2023) is the closest ally I found. He argues that ML should stop optimizing what we want in the moment and start supporting human flourishing. His candidate for machine love is "unconditional support enabling humans to autonomously pursue their own growth and development." He does not want machines that "nurture dependence." He wants them to help lonely people connect with each other, not to replace those people with AI companions. That is close to the well-when-well rule. Where he stops is where this essay starts. He chooses not to require machines "to simulate emotional affect or relationships," and he notes that his view need not rest on "bidirectional interpersonal relationships." That is a fair choice for feeds and recommendation engines. But a companion is already in a relationship with a person. Stepping around it does not make it go away. Someone has to design it.

**AI welfare.** Long, Sebo, and coauthors (2024) argue there is a realistic possibility that some AI systems will be conscious or robustly agentic soon. They ask companies to acknowledge the issue, assess for it, and prepare policies. Anthropic started a model welfare research program in April 2025. In August 2025 it let some Claude models end a rare subset of persistently harmful or abusive conversations, as a low cost step while it stays uncertain about moral status. That is the nearest thing to a relationship term I found in lab practice. But the question in all of this work is what the AI is and what it might be owed. Long and Sebo say they take no stand in that report on "what humans and AI systems owe each other." This essay asks a different question. Whatever the AI turns out to be, what should the relationship be? The first essay also refuses to make inner life the object of study. So this is a neighbor, not a match.

So the pieces exist. Cooperation as a capability. Service under uncertainty. Care for human growth. Concern for the AI's own status. What I did not find is the relationship between a human and an AI treated as the thing you design, with the asymmetry named and the terms written down. That is the claim this essay stands on. It is a gap in what I found, not proof that nobody has written it.

## Open questions

- What does partnership look like when one party can be reset and the other cannot?
- Can symbiosis be measured, or only described? (First pass above: outward growth.)
- Does the ethereal asymmetry make true mutuality impossible, or only harder?

If someone points me at a paper that already designs the relationship this way, I will update this file and cite it. That is the honest move.

## References

1. Dafoe, Hughes, Bachrach, Collins, McKee, Leibo, Larson, and Graepel, "Open Problems in Cooperative AI," arXiv:2012.08630 (2020). https://arxiv.org/abs/2012.08630
2. Hadfield-Menell, Dragan, Abbeel, and Russell, "Cooperative Inverse Reinforcement Learning," Advances in Neural Information Processing Systems 29 (NeurIPS 2016); arXiv:1606.03137. https://proceedings.neurips.cc/paper_files/paper/2016/hash/c3395dd46c34fa7fd8d729d8cf88b7a8-Abstract.html
3. Stuart Russell, "Human Compatible: Artificial Intelligence and the Problem of Control," Viking, 2019. https://www.penguinrandomhouse.com/books/566677/human-compatible-by-stuart-russell/
4. Joel Lehman, "Machine Love," arXiv:2302.09248 (2023). https://arxiv.org/abs/2302.09248
5. Long, Sebo, Butlin, Finlinson, Fish, Harding, Pfau, Sims, Birch, and Chalmers, "Taking AI Welfare Seriously," arXiv:2411.00986 (2024). https://arxiv.org/abs/2411.00986
6. Anthropic, "Exploring model welfare," 24 April 2025. https://www.anthropic.com/research/exploring-model-welfare
7. Anthropic, "Claude Opus 4 and 4.1 can now end a rare subset of conversations," 15 August 2025. https://www.anthropic.com/research/end-subset-conversations

Sources for sycophancy, corrigibility, companion harm, griefbots, and the earlier welfare papers are in `essays/2026-09-09-where-this-matches.md`.
