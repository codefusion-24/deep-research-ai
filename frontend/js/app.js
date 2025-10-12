/*
Save this as: frontend/js/app.js
Main React application
*/

function App() {
    const { useState, useEffect } = React;
    
    // State management
    const [query, setQuery] = useState('');
    const [maxTasks, setMaxTasks] = useState(5);
    const [isLoading, setIsLoading] = useState(false);
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);
    const [stage, setStage] = useState('');
    const [progress, setProgress] = useState(0);
    const [apiUrl, setApiUrl] = useState('http://localhost:8000');
    const [showSettings, setShowSettings] = useState(false);

    // Progress simulation stages
    const stages = [
        'Initializing research system...',
        'Decomposing query with Chain of Thought...',
        'Launching multi-agent search...',
        'Agent 1: Executing searches...',
        'Agent 2: Executing searches...',
        'Agent 3: Executing searches...',
        'Applying Self-Consistency validation...',
        'Extracting insights from sources...',
        'Generating comprehensive report with LLM...',
        'Formatting citations and sources...',
        'Finalizing research report...'
    ];

    // Handle research submission
    const handleResearch = async () => {
        if (!query.trim()) {
            setError('Please enter a research query');
            return;
        }

        setIsLoading(true);
        setError(null);
        setResult(null);
        setProgress(0);
        setStage(stages[0]);

        // Simulate progress with stages
        let stageIndex = 0;
        const progressInterval = setInterval(() => {
            setProgress(prev => {
                if (prev >= 95) return prev;
                return prev + Math.random() * 2;
            });
        }, 1000);

        const stageInterval = setInterval(() => {
            if (stageIndex < stages.length - 1) {
                stageIndex++;
                setStage(stages[stageIndex]);
            }
        }, 7000);

        try {
            // Update API config
            API_CONFIG.baseUrl = apiUrl;
            
            // Make API call
            const data = await apiClient.post('/run', {
                query: query,
                max_tasks: maxTasks
            });

            // Clear intervals
            clearInterval(progressInterval);
            clearInterval(stageInterval);

            // Set final state
            setProgress(100);
            setStage('Research complete! ✅');
            setResult(data);
            
        } catch (err) {
            clearInterval(progressInterval);
            clearInterval(stageInterval);
            setError(err.message);
            console.error('Research error:', err);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="min-h-screen p-6">
            <div className="max-w-7xl mx-auto">
                {/* Header */}
                <Header 
                    showSettings={showSettings} 
                    setShowSettings={setShowSettings} 
                />

                {/* Settings Panel */}
                {showSettings && (
                    <SettingsPanel 
                        apiUrl={apiUrl} 
                        setApiUrl={setApiUrl} 
                    />
                )}

                {/* Query Input */}
                <QueryInput
                    query={query}
                    setQuery={setQuery}
                    maxTasks={maxTasks}
                    setMaxTasks={setMaxTasks}
                    isLoading={isLoading}
                    onSubmit={handleResearch}
                />

                {/* Progress Bar */}
                {isLoading && (
                    <ProgressBar progress={progress} stage={stage} />
                )}

                {/* Error Display */}
                {error && (
                    <ErrorDisplay error={error} apiUrl={apiUrl} />
                )}

                {/* Results */}
                {result && (
                    <div className="space-y-6">
                        {/* Metrics */}
                        <MetricsRow result={result} />

                        {/* Planning Overview */}
                        <PlanningOverview planning={result.planning} />

                        {/* Executive Summary */}
                        <ExecutiveSummary summary={result.executive_summary} />

                        {/* Sections */}
                        {result.sections?.map((section, idx) => (
                            <SectionCard key={idx} section={section} index={idx} />
                        ))}

                        {/* Sources */}
                        <SourcesSection 
                            sources={result.all_sources || []} 
                            metadata={result.metadata || {}} 
                        />

                        {/* Verification */}
                        {result.verification && (
                            <VerificationSection verification={result.verification} />
                        )}

                        {/* Techniques */}
                        {result.metadata?.techniques_used && (
                            <TechniquesUsed techniques={result.metadata.techniques_used} />
                        )}

                        {/* Download */}
                        <DownloadSection result={result} />
                    </div>
                )}

                {/* Footer */}
                <Footer />
            </div>
        </div>
    );
}

// Render the app
ReactDOM.render(<App />, document.getElementById('root'));