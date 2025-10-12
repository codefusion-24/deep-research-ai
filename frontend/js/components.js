// Icons
const Icons = {
    Search: () => (
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
        </svg>
    ),
    Brain: () => (
        <svg className="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
        </svg>
    ),
    Check: () => (
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
        </svg>
    ),
    Link: () => (
        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
        </svg>
    ),
    Loader: () => (
        <svg className="animate-spin w-5 h-5" fill="none" viewBox="0 0 24 24">
            <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
            <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
    ),
    Settings: () => (
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
    ),
    Download: () => (
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
        </svg>
    )
};

// Header Component
function Header({ showSettings, setShowSettings }) {
    return (
        <div className="text-center mb-12 slide-in">
            <div className="flex items-center justify-center gap-4 mb-6">
                <div className="floating">
                    <Icons.Brain />
                </div>
                <h1 className="text-6xl font-black gradient-text">
                    Deep Research AI
                </h1>
            </div>
            <p className="text-xl text-gray-300 mb-4">
                Advanced Multi-Agent Research System
            </p>
            <div className="flex flex-wrap justify-center gap-2 text-sm">
                <span className="badge">Chain of Thought</span>
                <span className="badge">Multi-Agent</span>
                <span className="badge">Self-Consistency</span>
                <span className="badge">LLM Synthesis</span>
            </div>
            
            <button
                onClick={() => setShowSettings(!showSettings)}
                className="mt-6 px-4 py-2 glass-card hover:bg-white/10 transition-all rounded-lg text-sm flex items-center gap-2 mx-auto"
            >
                <Icons.Settings />
                <span>Settings</span>
            </button>
        </div>
    );
}

// Settings Panel Component
function SettingsPanel({ apiUrl, setApiUrl }) {
    return (
        <div className="glass-card p-6 mb-6 slide-in">
            <h3 className="text-xl font-semibold mb-4">⚙️ Configuration</h3>
            <div>
                <label className="block text-sm text-gray-400 mb-2">Backend API URL</label>
                <input
                    type="text"
                    value={apiUrl}
                    onChange={(e) => setApiUrl(e.target.value)}
                    className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-lg focus:outline-none focus:border-purple-500 transition-all text-white"
                    placeholder="http://localhost:8000"
                />
                <p className="text-xs text-gray-500 mt-2">
                    Change this if your backend is running on a different URL
                </p>
            </div>
        </div>
    );
}

// Query Input Component
function QueryInput({ query, setQuery, maxTasks, setMaxTasks, isLoading, onSubmit }) {
    return (
        <div className="glass-card p-8 mb-8 slide-in">
            <div className="space-y-6">
                <div>
                    <label className="block text-lg font-semibold mb-3 flex items-center gap-2">
                        <Icons.Search />
                        <span>Research Query</span>
                    </label>
                    <textarea
                        value={query}
                        onChange={(e) => setQuery(e.target.value)}
                        placeholder="Enter your research question... e.g., 'Analyze the competitive landscape of AI agents in 2024'"
                        rows="4"
                        className="w-full px-6 py-4 bg-white/5 border border-white/10 rounded-lg focus:outline-none focus:border-purple-500 transition-all text-white placeholder-gray-500 resize-none"
                        disabled={isLoading}
                    />
                </div>

                {/* Example Queries */}
                <div>
                    <p className="text-sm text-gray-400 mb-2">💡 Try these examples:</p>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                        {EXAMPLE_QUERIES.map((example, idx) => (
                            <button
                                key={idx}
                                onClick={() => setQuery(example)}
                                className="text-left px-4 py-2 bg-white/5 hover:bg-white/10 border border-white/10 hover:border-purple-500/50 rounded-lg text-sm text-gray-300 transition-all"
                                disabled={isLoading}
                            >
                                {example}
                            </button>
                        ))}
                    </div>
                </div>

                <div className="flex items-center gap-4">
                    <div className="flex-1">
                        <label className="block text-sm text-gray-400 mb-2">
                            Research Depth (Max Tasks)
                        </label>
                        <input
                            type="range"
                            value={maxTasks}
                            onChange={(e) => setMaxTasks(parseInt(e.target.value))}
                            min="3"
                            max="10"
                            className="w-full"
                            disabled={isLoading}
                        />
                        <div className="flex justify-between text-xs text-gray-500 mt-1">
                            <span>Quick (3)</span>
                            <span className="text-purple-400 font-semibold">{maxTasks}</span>
                            <span>Deep (10)</span>
                        </div>
                    </div>

                    <div className="flex-1 pt-6">
                        <button
                            onClick={onSubmit}
                            disabled={isLoading || !query.trim()}
                            className="w-full glow-button text-white font-semibold py-4 px-8 rounded-lg flex items-center justify-center gap-3 transition-all"
                        >
                            {isLoading ? (
                                <>
                                    <Icons.Loader />
                                    <span>Researching...</span>
                                </>
                            ) : (
                                <>
                                    <Icons.Search />
                                    <span>Start Research</span>
                                </>
                            )}
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
}

// Progress Component
function ProgressBar({ progress, stage }) {
    return (
        <div className="glass-card p-6 mb-8 slide-in">
            <div className="space-y-4">
                <div className="flex justify-between items-center">
                    <span className="text-sm font-medium stage-indicator">{stage}</span>
                    <span className="text-sm text-gray-400">{Math.round(progress)}%</span>
                </div>
                <div className="w-full bg-white/10 rounded-full h-3 overflow-hidden">
                    <div
                        className="progress-bar h-full rounded-full"
                        style={{ width: `${progress}%` }}
                    />
                </div>
                <div className="text-center text-sm text-gray-400 pulse">
                    ⏳ Please wait 30-90 seconds for comprehensive research...
                </div>
            </div>
        </div>
    );
}

// Error Component
function ErrorDisplay({ error, apiUrl }) {
    return (
        <div className="glass-card p-6 mb-8 border-red-500/50 slide-in">
            <div className="flex items-start gap-3">
                <span className="text-3xl">⚠️</span>
                <div>
                    <h3 className="font-semibold text-red-400 mb-2">Error</h3>
                    <p className="text-gray-300">{error}</p>
                    <p className="text-sm text-gray-500 mt-2">
                        Make sure your backend is running at {apiUrl}
                    </p>
                </div>
            </div>
        </div>
    );
}

// Metrics Row Component
function MetricsRow({ result }) {
    const metrics = [
        {
            value: result.execution_summary?.agents_deployed || 0,
            label: 'Agents',
            icon: '🤖'
        },
        {
            value: result.metadata?.total_sources || 0,
            label: 'Sources',
            icon: '📚'
        },
        {
            value: result.metadata?.high_confidence_sources || 0,
            label: 'Verified',
            icon: '⭐'
        },
        {
            value: result.planning?.total_searches || 0,
            label: 'Searches',
            icon: '🔍'
        },
        {
            value: `${result.execution_summary?.processing_time || 0}s`,
            label: 'Time',
            icon: '⏱️'
        }
    ];

    return (
        <div className="grid grid-cols-2 md:grid-cols-5 gap-4 mb-6">
            {metrics.map((metric, idx) => (
                <div key={idx} className="metric-card slide-in" style={{animationDelay: `${idx * 0.1}s`}}>
                    <div className="text-3xl mb-2">{metric.icon}</div>
                    <div className="text-3xl font-bold gradient-text mb-1">
                        {metric.value}
                    </div>
                    <div className="text-xs text-gray-400">{metric.label}</div>
                </div>
            ))}
        </div>
    );
}

// Planning Overview Component
function PlanningOverview({ planning }) {
    if (!planning) return null;

    return (
        <div className="glass-card p-6 mb-6 fade-in">
            <h2 className="text-2xl font-bold mb-4 flex items-center gap-3">
                🧠 Research Strategy
            </h2>
            <p className="text-gray-400 mb-4">
                Strategy: <span className="text-purple-400 font-semibold">{planning.decomposition_strategy}</span>
            </p>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {planning.dimensions?.map((dim, idx) => (
                    <div key={idx} className="agent-card complete">
                        <div className="flex items-center gap-2 mb-2">
                            <span className="text-lg font-semibold">🤖 Agent {idx + 1}</span>
                        </div>
                        <h4 className="font-semibold text-sm mb-2">{dim.aspect}</h4>
                        <p className="text-xs text-gray-400 mb-3">{dim.rationale}</p>
                        <div className="text-xs">
                            <span className="badge-info badge">{dim.queries?.length} searches</span>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

// Executive Summary Component
function ExecutiveSummary({ summary }) {
    return (
        <div className="glass-card p-6 mb-6 fade-in">
            <h2 className="text-2xl font-bold mb-4 flex items-center gap-3">
                📄 Executive Summary
            </h2>
            <div className="prose prose-invert max-w-none">
                <p className="text-gray-300 leading-relaxed whitespace-pre-wrap">
                    {summary}
                </p>
            </div>
        </div>
    );
}

// Section Card Component
function SectionCard({ section, index }) {
    const [expanded, setExpanded] = React.useState(false);

    return (
        <div className="section-card slide-in" style={{animationDelay: `${index * 0.1}s`}}>
            <div className="flex items-start justify-between mb-4">
                <h3 className="text-xl font-bold flex items-center gap-2">
                    <span className="text-2xl">{index + 1}</span>
                    <span>{section.title}</span>
                </h3>
                <div className="flex gap-2">
                    <span className="badge-success badge text-xs">
                        {section.source_count} sources
                    </span>
                    <span className="badge-warning badge text-xs">
                        {section.high_confidence_count} verified
                    </span>
                </div>
            </div>
            
            <div className="prose prose-invert max-w-none mb-4">
                <p className="text-gray-300 leading-relaxed whitespace-pre-wrap">
                    {section.content}
                </p>
            </div>
            
            {section.key_points && section.key_points.length > 0 && (
                <details className="mt-4" open={expanded} onToggle={(e) => setExpanded(e.target.open)}>
                    <summary className="cursor-pointer text-purple-400 font-semibold mb-3 hover:text-purple-300 flex items-center gap-2">
                        🔍 View Key Findings ({section.key_points.length})
                    </summary>
                    <div className="space-y-3 mt-3">
                        {section.key_points.map((point, pidx) => (
                            <div 
                                key={pidx} 
                                className={`source-card p-3 bg-white/5 rounded-lg ${point.is_high_confidence ? 'high-confidence' : ''}`}
                            >
                                <div className="flex items-start gap-2">
                                    {point.is_high_confidence ? (
                                        <span className="text-green-400 text-lg">⭐⭐</span>
                                    ) : (
                                        <span className="text-yellow-400 text-lg">⭐</span>
                                    )}
                                    <div className="flex-1">
                                        <p className="text-gray-300 text-sm mb-2">{point.text}</p>
                                        {point.source && (
                                            <a
                                                href={point.source.url}
                                                target="_blank"
                                                rel="noopener noreferrer"
                                                className="text-blue-400 hover:text-blue-300 text-xs flex items-center gap-1"
                                            >
                                                <Icons.Link />
                                                <span>{point.source.title}</span>
                                            </a>
                                        )}
                                        {point.is_high_confidence && (
                                            <span className="badge-success badge text-xs mt-2 inline-block">
                                                Cross-validated
                                            </span>
                                        )}
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                </details>
            )}
        </div>
    );
}

// Sources Component
function SourcesSection({ sources, metadata }) {
    const [activeTab, setActiveTab] = React.useState('all');
    
    const displaySources = activeTab === 'all' 
        ? sources 
        : sources.filter(s => s.confidence >= 2);

    return (
        <div className="glass-card p-6 mb-6 fade-in">
            <h2 className="text-2xl font-bold mb-4 flex items-center gap-3">
                🔗 Research Sources ({sources.length})
            </h2>
            
            <div className="flex gap-2 mb-4">
                <button
                    onClick={() => setActiveTab('all')}
                    className={`px-4 py-2 rounded-lg transition-all ${
                        activeTab === 'all' 
                            ? 'bg-purple-600' 
                            : 'bg-white/5 hover:bg-white/10'
                    }`}
                >
                    All Sources
                </button>
                <button
                    onClick={() => setActiveTab('verified')}
                    className={`px-4 py-2 rounded-lg transition-all ${
                        activeTab === 'verified' 
                            ? 'bg-green-600' 
                            : 'bg-white/5 hover:bg-white/10'
                    }`}
                >
                    Verified Only ({metadata.high_confidence_sources})
                </button>
            </div>

            <div className="space-y-3 max-h-96 overflow-y-auto scrollbar-custom pr-2">
                {displaySources.slice(0, 30).map((source, idx) => (
                    <a
                        key={idx}
                        href={source.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className={`source-card flex items-start gap-3 p-4 bg-white/5 rounded-lg hover:bg-purple-500/10 border border-white/10 ${
                            source.confidence >= 2 ? 'high-confidence' : ''
                        }`}
                    >
                        <span className="flex items-center justify-center min-w-8 h-8 rounded-full bg-purple-500/20 text-purple-400 font-semibold text-sm">
                            {idx + 1}
                        </span>
                        <div className="flex-1">
                            <div className="flex items-start justify-between gap-2 mb-1">
                                <h4 className="font-medium text-gray-200">{source.title}</h4>
                                {source.confidence >= 2 && (
                                    <span className="badge-success badge text-xs whitespace-nowrap">
                                        ⭐ {source.confidence}x
                                    </span>
                                )}
                            </div>
                            {source.snippet && (
                                <p className="text-gray-400 text-sm mb-2 line-clamp-2">
                                    {source.snippet}
                                </p>
                            )}
                            <div className="flex items-center gap-2 text-xs text-blue-400">
                                <Icons.Link />
                                <span className="truncate">{source.url}</span>
                            </div>
                        </div>
                    </a>
                ))}
            </div>
        </div>
    );
}

// Verification Component
function VerificationSection({ verification }) {
    return (
        <div className="glass-card p-6 mb-6 fade-in">
            <h2 className="text-2xl font-bold mb-4 flex items-center gap-3">
                ✅ Verification & Validation
            </h2>
            <div className="space-y-4">
                {verification.map((item, idx) => (
                    <div key={idx} className="p-4 bg-green-500/10 border border-green-500/30 rounded-lg">
                        <div className="flex items-start gap-3">
                            <Icons.Check />
                            <div className="flex-1">
                                <p className="text-gray-200 font-medium mb-2">{item.claim}</p>
                                <div className="flex flex-wrap gap-2">
                                    {item.supported_by.map((support, sidx) => (
                                        <span key={sidx} className="badge-success badge text-xs">
                                            {support}
                                        </span>
                                    ))}
                                </div>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

// Techniques Component
function TechniquesUsed({ techniques }) {
    return (
        <div className="glass-card p-6 mb-6 fade-in">
            <h2 className="text-2xl font-bold mb-4">🧮 Advanced Techniques Applied</h2>
            <div className="grid grid-cols-2 md:grid-cols-5 gap-3">
                {techniques.map((technique, idx) => (
                    <div 
                        key={idx} 
                        className="text-center p-4 bg-gradient-to-br from-purple-500/20 to-pink-500/20 rounded-lg border border-purple-500/30"
                    >
                        <div className="text-2xl mb-2">✨</div>
                        <div className="text-sm font-semibold text-gray-200">{technique}</div>
                    </div>
                ))}
            </div>
        </div>
    );
}

// Download Component
function DownloadSection({ result }) {
    const handleDownloadMarkdown = () => {
        const markdown = reportGenerator.toMarkdown(result);
        reportGenerator.download(markdown, `research-${Date.now()}.md`, 'text/markdown');
    };

    const handleDownloadJSON = () => {
        const json = JSON.stringify(result, null, 2);
        reportGenerator.download(json, `research-${Date.now()}.json`, 'application/json');
    };

    return (
        <div className="glass-card p-6 text-center fade-in">
            <h3 className="text-xl font-bold mb-4 flex items-center justify-center gap-2">
                <Icons.Download />
                Export Research Report
            </h3>
            <div className="flex flex-wrap justify-center gap-4">
                <button
                    onClick={handleDownloadMarkdown}
                    className="px-6 py-3 bg-gradient-to-r from-purple-600 to-pink-600 rounded-lg font-semibold hover:from-purple-700 hover:to-pink-700 transition-all flex items-center gap-2"
                >
                    <Icons.Download />
                    Download Markdown
                </button>
                <button
                    onClick={handleDownloadJSON}
                    className="px-6 py-3 bg-gradient-to-r from-blue-600 to-cyan-600 rounded-lg font-semibold hover:from-blue-700 hover:to-cyan-700 transition-all flex items-center gap-2"
                >
                    <Icons.Download />
                    Download JSON
                </button>
            </div>
        </div>
    );
}

// Footer Component
function Footer() {
    return (
        <div className="text-center mt-12 text-gray-500 text-sm">
            <div className="flex items-center justify-center gap-4 mb-2">
                <span>Powered by gpt-4o & SerpAPI</span>
                <span>•</span>
                <span>Deep Research AI v1.0</span>
            </div>
            <div className="flex items-center justify-center gap-2 text-xs">
                <span className="px-2 py-1 bg-green-500/20 text-green-400 rounded">
                    Backend Connected
                </span>
                <span className="px-2 py-1 bg-blue-500/20 text-blue-400 rounded">
                    Multi-Agent Active
                </span>
            </div>
        </div>
    );
}
