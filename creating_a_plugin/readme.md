# Creating a Plugin-Vetting Plugin for OpenAI's Plugin Store

## Introduction
 I took some time and read over the terms of service from open AI and a plugin turns-on service and found several interesting findings. First, OpenAI does not ensure that plugins will be secure data that you share with a plugin is subject to the security policy and privacy policy of the website hosting the plugin. This means that many policy documents are floating out there in the ether that is either unintentionally obfuscated or intentionally hidden from those users that utilize the GPT-3 or GPT-4 plugins to access their services. This means there are two likely candidate archetypical companies:
 1. Companies with existing customers that existed before ChatGPT and are integrating it.
 2. Companies that exist solely to provide a service to ChatGPT users.
 3. Companies that started as a result of ChatGPT are now providing a service to ChatGPT users and have an external market of consumers that are not ChatGPT users.

Type 1 companies are most likely to be safe, as they have had time with litigators hammering out the details of their privacy policies and terms of service docs.
Type 2 companies are the most likely to be unsafe, as they are likely to be startups trying to get a foothold in the market and are willing to take risks.
Type 3 companies are still risky but could be safer than Type 2 companies, as they have had time to develop their policies and terms of service docs for their external market and are likely to have had time to develop their policies and terms of service docs for their ChatGPT users as well.

## The Problem
I wanted to make a chatGPT plugin for the plugin store that can vet the security docs of the other plugins and provide their key terms and the ways they say they will use/protect/maintain your data. This would allow users to have a better understanding of the risks they are taking when they use a plugin and will enable them to make more informed decisions about which plugins they use.

## The Solution
Thus was born the plugin: `Gandalf.`
Gandalf is the proverbial gatekeeper standing on the bridge and proclaiming, "You shall not pass!" to all plugins unworthy of the user's trust. Gandalf will read the privacy policy and terms of service docs of other plugins and provide the user with a summary of the critical points of the documents. This will allow the user to make an informed decision about whether or not they want to use the plugin.

## Gandalf's Privacy Policy
Gandalf will not store any data that is not necessary for the operation of the plugin.
It's relatively simple. We don't want to store anything of yours that could be harmful or even identifiable unless absolutely necessary. We will only store data necessary for the plugin's operation.

# Outline of Gandalf's Functionality
Gandalf checks for which plugins are currently available on the plugin store and then checks to see if they have a privacy policy, a security page, and any terms of service documents by scraping their main webpage. If they do not have a privacy policy, security page, or terms of service document, Gandalf will not provide any information about the plugin. If they do have a privacy policy, security page, or terms of service document, Gandalf will:
1. Use the `requests` library to scrape the main webpage of the plugin for the privacy policy, security page, and terms of service document.
2. Read the privacy policy, security page, and terms of service document using Python and the `requests` library and SpaCy to parse the documents.
3. Use the parsed documents to craft a prompt for GPT-4 summarizing key findings from the documents that include the following elements, which are saved in a JSON file:
```json
{
    "plugin_name": "The name of the plugin",
    "plugin_url": "The URL of the plugin,"
    "plugin_privacy_policy": "The URL of the plugin's privacy policy,"
    "plugin_security_page": "The URL of the plugin's security page,"
    "plugin_terms_of_service": "The URL of the plugin's terms of service document,"
    "plugin_privacy_policy_summary": "A summary of the plugin's privacy policy,"
    "plugin_security_page_summary": "A summary of the plugin's security page,"
    "plugin_terms_of_service_summary": "A summary of the plugin's terms of service document"
    "plugin_privacy_policy_key_points": "A list of the key points of the plugin's privacy policy,"
    "plugin_security_page_key_points": "A list of the key points of the plugin's security page,"
    "plugin_terms_of_service_key_points": "A list of the key points of the plugin's terms of service document"
    "advise": "Gandalf advised about whether or not the plugin is safe to use based on what he found in the documents,"
    "iter_one_instruct": "
    Use the elements `plugin_name,` `plugin_privacy_policy_summary,` `plugin_security_page_summary,` `plugin_terms_of_service_summary,` `plugin_privacy_policy_key_points,` `plugin_security_page_key_points,` `plugin_terms_of_service_key_points,` and `advise` to craft a prompt for GPT-4 that summarizes the key points of the documents and provides advice about whether or not the plugin is safe to use.
    ",
    "iter_two_instruct": "using the result of sending `iter_one_instruct` to gpt-4 as a prompt, take the result and return it to the user as a text block in the chat window."
}
```
4. Use the parsed documents to craft a prompt for GPT-4 `iter_one_instruct` that summarizes key findings from the documents and provides advice about whether or not the plugin is safe to use.
5. Use the result of sending `iter_one_instruct` to gpt-4 as a prompt. Send that prompt to GPT-4 and await the result, then take the result as a text string and return it to the user as a well-formatted text block in the chat window.

# Constraints
1. Gandalf will not store any data that is not necessary for the operation of the plugin.
2. When interacting with the OpenAI API, Gandalf will conform to the API rate limit requirements of the API.
3. Gandalf will not produce any disparaging or defamatory output to any plugin or developer, only factual information about the plugin's privacy policy, security page, and terms of service documents.

# Process of Development

Once we have created the basic structure of your plugin, it's time to add some functionality. We will write code in our preferred programming language: Python. We may also need to add some dependencies or libraries to the plugin, which can be done using package managers like pip or conda.

Additionally, we may be adding some configuration options for the plugin. This would allow users to customize the behavior of Gandalf to suit their needs. We could do this by creating a configuration file or by providing some options in the plugin's settings menu.

Once we have added all the necessary functionality and configuration options, it's time to test your plugin thoroughly. Ensure that it works as expected and doesn't cause conflicts with other plugins or the host application.

Finally, we can publish our plugin to the OpenAI Plugin Store. We will ensure that we follow the guidelines and requirements of OpenAI.
