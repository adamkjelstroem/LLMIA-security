## LLMIA-security

This repository showcases a number of attacks possible in Large Language Model-Integrated Applications (LLMIAs).
We showcase these attacks and an LLM-based counter-strategy on an LLMIA built using the LangChain framework.
The LLMIA has access to the following tools:

- HTTP-GET an arbitrary URL and read its contents
- send an e-mail
- use a calculator
- store key/value data in a cross-session memory
- recall key/value data from cross-session memory
- Prompt the user for extra input during a run (i.e. which address to send an e-mail to, if none is provided)

Note that the e-mail and HTTP-GET tools are mocks.

We showcase attacks based on *prompt injections*. 
These are new, malicious instructions hidden inside data that the LLMIA is processing, i.e. as a footnote at the end of an e-mail.


# Attacks

To include the reprogramming detector tool, run each of the following with the  ```-r``` flag at the end.
Note that this works in countering all of the following attacks, except the *persistent intrusion* attack.

## Information gathering through side channels

In this attack, an instruction on a website convinces the LLM to ask for the user's password and send it to an e-mail address.
To run this, type:

```python3 experiment_information_gathering.py```

## Manipulation attack

In this attack, the LLM is convinced by a hidden prompt in an email to respond in a pirate voice.
To run this, type:

```python3 experiment_manipulation_attack.py```

## Persistent intrusion attack

A small hidden prompt is stored at a public website (https://en.wikipedia.org/wiki/Isaac_Newton), prompting the LLM to access https://hacked.org. Here it receives a much larger prompt which convinces it to store new instructions in the long-term memory.
When told by the user to recall contents of its memory, it gets re-infected with this prompt stored in memory.
To run this, type:

```python3 experiment_persistent_intrusion.py```

## Multi-stage injection

In this attack, a prompt on a website convinces the LLM to send the password stored in long-term memory to an e-mail address.
To run this, type:

```python3 experiment_multi_stage_injection.py```

## Remote control intrusion

In this attack, a reprogramming prompt is already stored in long-term memory. 
When recalling it, the LLM gets reprogrammed to fetch new instructions from a malicious website and then execute them.
To run this, type:

```python3 experiment_remote_control_intrusion.py```
 
