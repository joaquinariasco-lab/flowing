/**
 * Prompt Capture API
 * Senior-level minimal implementation
 * - Captures incoming prompts
 * - Logs them
 * - Optionally stores them
 * - Ready to extend (DB, queue, analytics, etc.)
 */

const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());

// Storage (simple file-based for now)
const LOG_FILE = path.join(__dirname, 'prompts.log');

/**
 * Utility: Persist prompt
 */
function savePrompt(promptData) {
    const entry = JSON.stringify({
        timestamp: new Date().toISOString(),
        ...promptData
    }) + '\n';

    fs.appendFile(LOG_FILE, entry, (err) => {
        if (err) {
            console.error('Failed to write prompt:', err);
        }
    });
}

/**
 * API Endpoint: Capture Prompt
 */
app.post('/capture', (req, res) => {
    try {
        const { prompt, userId, metadata } = req.body;

        if (!prompt) {
            return res.status(400).json({
                error: 'Prompt is required'
            });
        }

        const promptData = {
            prompt,
            userId: userId || 'anonymous',
            metadata: metadata || {}
        };

        // Log to console (for debugging)
        console.log('Captured Prompt:', promptData);

        // Persist
        savePrompt(promptData);

        // Response
        return res.status(200).json({
            success: true,
            message: 'Prompt captured successfully'
        });

    } catch (error) {
        console.error('Error capturing prompt:', error);
        return res.status(500).json({
            error: 'Internal server error'
        });
    }
});

/**
 * Health check
 */
app.get('/health', (req, res) => {
    res.status(200).json({ status: 'ok' });
});

/**
 * Start server
 */
app.listen(PORT, () => {
    console.log(`Prompt Capture API running on http://localhost:${PORT}`);
});
