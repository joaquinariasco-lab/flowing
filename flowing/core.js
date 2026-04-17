import fetch from "node-fetch";

/**
 * Sends a prompt to the AI API and returns the response.
 * @param {string} prompt - The developer's input prompt
 * @param {string} apiKey - The developer's API key
 * @returns {Promise<string>}
 */
export async function getAIResponse(prompt, apiKey) {
    if (!prompt || typeof prompt !== "string") {
        throw new Error("Invalid prompt");
    }

    if (!apiKey) {
        throw new Error("API key is required");
    }

    try {
        const response = await fetch("https://api.openai.com/v1/responses", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                model: "gpt-5.3",
                input: prompt
            })
        });

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`API Error: ${response.status} - ${errorText}`);
        }

        const data = await response.json();

        // Normalize response safely
        const output = data.output?.[0]?.content?.[0]?.text;

        if (!output) {
            throw new Error("Invalid response format from API");
        }

        return output;

    } catch (error) {
        console.error("AI request failed:", error.message);
        throw error;
    }
}
