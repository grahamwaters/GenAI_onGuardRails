# GenAI on GuardRails
Protecting your PID, IP, and Company secrets while using GenAI.

# Introduction

Building Guardrails for Yourself and Your Company with Python while Using Generative AI Tools

Data scientists, analysts, and every person across a multidisciplinary spectrum at any organization must consider implementing guardrails immediately for their employees that don't limit the potential of how AI will revolutionize the world but keep it in check to prevent their PII and IP from slipping into the ether of the regenerative reinforcement algorithm that feeds OpenAI's excellent new toolkit. In addition, It's easy to assume that the machine must be correct because it usually is. But in reality, a machine is simply a mechanical brain, and brains are sometimes wrong and even hallucinate. We must discuss these topics to move forward as organizations that thrive in the new age of AI.


# Preface
This is a simple guide to help you protect your PID, IP, and Company secrets while using GenAI. This guide is not meant to be a comprehensive guide to security, but rather a simple guide to help you get started.

There are many facets to consider when securing your GenAI environment. To hone in on the "one thing" (to quote Gary Keller and Jay Papasan) that you can do to protect your PID, IP, and Company secrets, is difficult because it's an evolving issue. There are more and more tools being developed every day that can counterman the latest security threats, while equal numbers of vectors for attack are being developed. Something we often forget is that security is a process, not a destination. It's a journey, not a destination. It's a marathon, not a sprint. It's a bunch of other cliches as well. The point is, security is a process that requires constant vigilance and attention. It's not something you can set and forget. It's not something you can do once and be done with it. It's something you have to constantly be aware of and constantly be working on.

At engage2Learn I've been working with our Tiger Team to develop security protocols for how we can and cannot use GenAI. This is a living document that will be updated as we learn more about the security landscape and as we develop more tools to help us protect our PID, IP, and Company secrets. I heard the other day that with only 15 data points a person's anonymized PID can be identified with 99.98% accuracy. Fifteen may seem like a lot of data points at first, but in actuality, think of how many lines you fill out when you use a website, go to the doctor, or even just use your phone. It's not hard to get to 15 data points. And once you're there, you're no longer anonymous.
"""
“We need to move beyond de-identification,” he said. “Anonymity is not a property of a data set, but is a property of how you use it.”
The balance is tricky: Information that becomes completely anonymous also becomes less useful, particularly to scientists trying to reproduce the results of other studies. But every small bit that is retained in a database makes identification of individuals more possible.

“Very quickly, with a few bits of information, everyone is unique,” said Dr. Erlich.
"""

<div align="center">
<h1> A.I.R.G.A.P. </h1>
<h2> Guardrails for the new GenAI-Age </h2>
</div>

# Assemble
Form a team of experts within your company that will be responsible for developing your security protocols. This team should include at least one person from each of the following departments: IT, Legal, HR, and Marketing. This team will be responsible for developing your security protocols and for training your employees on how to use GenAI securely. Once you have
# Inform
Inform your employees that they must stop all use of chatGPT and any GenAI tools until further notice. It is clearly stated in the privacy policies of OpenAI products that ANY text that is used in the web-interface (by non-opted-out users) will be used for model retraining and could be generated as a response to anyone in the world.
# Refine
Refine your security protocols based on feedback from your employees. Find out what they like to use GenAI for and what makes their lives easier and more productive. Find out what they don't like about GenAI and what makes their lives more difficult and less productive. Find out what they would like to see in the future and what they would like to see in the future.
# Generate Buy-In
Get buy-in from your employees by explaining to them why it's important to protect their PID, IP, and Company secrets. Show them how easily their PID can be identified with only 15 data points. Show them how easily their IP can be stolen. Or how easily their Company secrets can be leaked.
# Assess
How are you currently using GenAI? What are the risks associated with your current use of GenAI? What are the benefits? What are the risks associated with not using GenAI?
# Personalization/Protection/Privacy
How do we use protocols to both generate Python code with GenAI and simultaneously protect our PID, IP, and Company secrets?


# Python

## Example 1: Data Anonymization

One of the most common ways to protect PII (Personally Identifiable Information) is to anonymize the data before feeding it into the AI model. Here's a simple example of how you can do this using Python:

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Assume we have a dataframe df with some PII
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com'],
    # other non-PII columns...
})

# We can use LabelEncoder to anonymize the PII columns
encoder = LabelEncoder()

# Anonymize the 'name' column
df['name'] = encoder.fit_transform(df['name'])

# Anonymize the 'email' column
df['email'] = encoder.fit_transform(df['email'])

print(df)
```

## Example 2: Data Access Control

Another important aspect of protecting IP (Intellectual Property) is to control who has access to the data. Here's an example of how you can use Python to manage data access:

```python
import os
from getpass import getpass

# Ask for the user's password
password = getpass("Enter your password: ")

# Check if the password is correct
if password == os.environ['SECRET_PASSWORD']:
    # If the password is correct, allow access to the data
    print("Access granted.")
    # Load and process the data...
else:
    # If the password is incorrect, deny access
    print("Access denied.")
```

## Example 3: Model Interpretability

To prevent AI from making mistakes, it's important to understand how the model is making its decisions. Here's an example of how you can use Python to interpret a machine learning model using the SHAP library:

```python
import shap
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

# Load the breast cancer dataset
data = load_breast_cancer()
X_train, X_test, Y_train, Y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=0)

# Train a RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, Y_train)

# Use SHAP to explain the model's predictions
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Visualize the first prediction's explanation
shap.initjs()
shap.force_plot(explainer.expected_value[0], shap_values[0][0], X_test[0])
```

# Here are some GitHub repositories that address the challenges of privacy protection and data security in AI:

1. [**PySyft**](https://github.com/OpenMined/PySyft): PySyft is a Python library for secure, private computations in deep learning, using federated learning, differential privacy, and encrypted computation.

    Example code:
    ```python
    import syft as sy
    hook = sy.TorchHook(torch)
    bob = sy.VirtualWorker(hook, id="bob")
    x = torch.tensor([1,2,3,4,5])
    x = x.send(bob)
    bob._objects
    ```

2. [**Differential Privacy Library**](https://github.com/IBM/differential-privacy-library): This library from IBM provides a suite of tools to help you add differential privacy to your Python code.

    Example code:
    ```python
    from diffprivlib.models import GaussianNB
    clf = GaussianNB()
    clf.fit(X_train, y_train)
    ```

3. [**TensorFlow Privacy**](https://github.com/tensorflow/privacy): This library provides implementations of TensorFlow optimizers for training machine learning models with differential privacy.

    Example code:
    ```python
    from tensorflow_privacy.privacy.optimizers.dp_optimizer import DPGradientDescentGaussianOptimizer
    optimizer = DPGradientDescentGaussianOptimizer(
        l2_norm_clip=l2_norm_clip,
        noise_multiplier=noise_multiplier,
        num_microbatches=num_microbatches)
    ```

4. [**PyCryptodome**](https://github.com/Legrandin/pycryptodome): A self-contained cryptographic library for Python.

    Example code:
    ```python
    from Crypto.Cipher import AES
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    ```

5. [**Privacy Flash Pro**](https://github.com/privacy-tech-lab/privacyflash-pro): This tool generates a privacy policy for iOS apps by analyzing their code.

    Example code:
    ```python
    python3 scan.py /path/to/your/project
    ```

6. [**OpenAI Gym**](https://github.com/openai/gym): A toolkit for developing and comparing reinforcement learning algorithms.

    Example code:
    ```python
    import gym
    env = gym.make('CartPole-v0')
    env.reset()
    for _ in range(1000):
        env.render()
        env.step(env.action_space.sample()) # take a random action
    env.close()
    ```

7. [**PyTorch DP**](https://github.com/facebookresearch/pytorch-dp): A library for training PyTorch models with differential privacy.

    Example code:
    ```python
    from opacus import PrivacyEngine
    model = torch.nn.Linear(16, 32)  # An example model
    privacy_engine = PrivacyEngine(
        model,
        sample_rate=0.01,
        alphas=[10, 100],
        noise_multiplier=1.3,
        max_grad_norm=1.0,
    )
    privacy_engine.attach(optimizer)
    ```

8. [**Pyswarms**](https://github.com/ljvmiranda921/pyswarms): A research toolkit for particle swarm optimization in Python.

    Example code:
    ```python
    import pyswarms as ps
    options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
    optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)
    cost, pos = optimizer.optimize(sphere_func, iters=100)
    ```

9. [**CyberSecTK**](https://github.com/IBM/CyberSecTK): A Python library for preprocessing and feature extraction of cyber-security-related data.

    Example code:
    ```python
    from CyberSecTK import preprocessing
    data = preprocessing.remove_stop_words(data)
    ```

10. [**PyXhon**](https://github.com/PyXhon/Security): A security enhancement plug-in that detects security vulnerabilities and privacy leaks from third-party extensions.

    Example code:
    ```python
    import PyXhon
    PyXhon.scan('path_to_your_python_file')
    ```

These repositories provide a variety of tools and techniques to address the challenges of privacy, security, and data protection in AI and Python applications. They include libraries for differential privacy, cryptographic operations, secure computation, and more.

# Sources
[1](https://www.nytimes.com/2019/07/23/health/data-privacy-protection.html)
["15 Data Point Re-identification"](https://www.nature.com/articles/s41467-019-10933-3)
["OpenAI Democratic Policy Challenge"](https://openai.com/blog/democratic-inputs-to-ai)

# Authors
- [**Graham Waters**]()

# Acknowledgements
- Special thanks to gpt-4, github copilot, chatGPT as supplementary material generators.
