/*
Save this as: frontend/js/utils.js
Helper functions and utilities
*/

// API Configuration
const API_CONFIG = {
    baseUrl: 'http://localhost:8000',
    timeout: 120000 // 2 minutes
};

// API Client
const apiClient = {
    async fetch(endpoint, options = {}) {
        const url = `${API_CONFIG.baseUrl}${endpoint}`;
        const config = {
            ...options,
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            }
        };

        try {
            const response = await fetch(url, config);
            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.detail || `HTTP ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    },

    async get(endpoint) {
        return this.fetch(endpoint, { method: 'GET' });
    },

    async post(endpoint, data) {
        return this.fetch(endpoint, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }
};

// Report Generator
const reportGenerator = {
    toMarkdown(result) {
        let markdown = `# ${result.query}\n\n`;
        markdown += `**Generated:** ${new Date().toLocaleString()}\n`;
        markdown += `**Processing Time:** ${result.execution_summary?.processing_time}s\n\n`;
        markdown += `---\n\n`;
        
        // Executive Summary
        markdown += `## Executive Summary\n\n${result.executive_summary}\n\n---\n\n`;
        
        // Sections
        result.sections?.forEach((section, idx) => {
            markdown += `## ${idx + 1}. ${section.title}\n\n${section.content}\n\n`;
            
            if (section.key_points?.length > 0) {
                markdown += `### Key Findings\n\n`;
                section.key_points.forEach(point => {
                    const conf = point.is_high_confidence ? '⭐⭐' : '⭐';
                    markdown += `${conf} ${point.text}\n`;
                    if (point.source) {
                        markdown += `   *Source: [${point.source.title}](${point.source.url})*\n`;
                    }
                    markdown += `\n`;
                });
            }
            markdown += `---\n\n`;
        });
        
        // Sources
        markdown += `## Sources\n\n`;
        result.all_sources?.forEach((source, idx) => {
            markdown += `${idx + 1}. [${source.title}](${source.url})`;
            if (source.confidence >= 2) {
                markdown += ` ⭐ Verified ${source.confidence}x`;
            }
            markdown += `\n`;
        });
        
        markdown += `\n---\n\n## Metadata\n\n`;
        markdown += `- **Total Sources:** ${result.metadata?.total_sources}\n`;
        markdown += `- **High Confidence:** ${result.metadata?.high_confidence_sources}\n`;
        markdown += `- **Agents:** ${result.execution_summary?.agents_deployed}\n`;
        markdown += `- **Techniques:** ${result.metadata?.techniques_used?.join(', ')}\n`;
        
        return markdown;
    },

    download(content, filename, type = 'text/markdown') {
        const blob = new Blob([content], { type });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        a.click();
        URL.revokeObjectURL(url);
    }
};

// Example queries
const EXAMPLE_QUERIES = [
    "Analyze the competitive landscape of AI agents in 2024",
    "Latest developments in quantum computing",
    "Electric vehicle market trends 2024",
    "Impact of generative AI on software development",
    "Future of renewable energy technologies",
    "Blockchain adoption in enterprise 2024"
];