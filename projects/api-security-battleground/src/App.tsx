import { useState } from "react";

const TABS = ["Market Overview", "Battle Card", "Feature Matrix", "Activity Feed", "AI Advisor"];

// ─── Data ───
const marketData = {
  size2025: "1.1",
  size2030: "4.6",
  cagr: "~30%",
  attacks: "150B+",
  timeline: [
    { year: "2024 Jun", event: "Akamai acquires Noname for ~$450M" },
    { year: "2025 Feb", event: "Traceable merges into Harness (~$5B combined)" },
    { year: "2025 Jul", event: "Wallarm raises $55M Series C" },
    { year: "2025 Oct", event: "Levo launches unified AI Security platform" },
    { year: "2026 Jan", event: "Levo adds AI Firewall, MCP security, AI Gateway" },
  ],
};

const competitors = [
  { name: "Salt Security", funding: 281, employees: 201, color: "#ef4444" },
  { name: "Traceable/Harness", funding: 110, employees: 1100, color: "#f59e0b" },
  { name: "Noname/Akamai", funding: 220, employees: 500, color: "#8b5cf6" },
  { name: "Wallarm", funding: 81, employees: 163, color: "#06b6d4" },
  { name: "Akto", funding: 13, employees: 22, color: "#22c55e" },
  { name: "Levo.ai", funding: 4, employees: 38, color: "#3b82f6" },
];

const battleCard = {
  name: "Salt Security",
  tagline: "Most funded pure-play API security vendor",
  funding: "$281M (Series D, $1.4B valuation)",
  employees: "~201",
  hq: "Palo Alto, CA",
  customers: "Equinix, Zoom, Finastra, DeinDeal",
  weaknesses: [
    { point: "No native runtime blocking", detail: "Cannot block attacks inline — requires integration with third-party WAF or gateway" },
    { point: "Privacy-heavy architecture", detail: "Full API traffic sent to Salt's SaaS cloud for analysis — a red flag for regulated industries" },
    { point: "Reporting limitations", detail: "Users report inflexible dashboards and difficulty exporting custom reports (G2 reviews)" },
    { point: "UI performance at scale", detail: "Dashboard slows noticeably with large API inventories (Gartner Peer Insights feedback)" },
  ],
  howWeWin: [
    { point: "Privacy-first architecture", detail: "Less than 1% of data leaves customer environment vs. Salt sending full traffic to their cloud" },
    { point: "Native inline blocking", detail: "Levo blocks threats at runtime natively — no third-party integration needed" },
    { point: "Unified API + AI security", detail: "Single platform covers APIs, LLMs, MCP servers, AI agents — Salt only recently added basic MCP monitoring" },
    { point: "Capital efficiency = focus", detail: "$4M funding proves architectural superiority — not VC subsidy masking weak unit economics" },
  ],
  objections: [
    {
      q: "Levo only raised $4M. Salt raised $281M. Can you survive?",
      a: "Our capital efficiency reflects our architectural advantage. We deliver equal or better capabilities with 1/70th the funding. We're a Gartner Market Guide recommended vendor serving demanding fintech customers. Meanwhile, Salt's $1.4B valuation has come under pressure — more funding doesn't mean better product.",
    },
    {
      q: "Salt has more enterprise customers and case studies.",
      a: "Salt had a 3-year head start. But ask their customers about runtime blocking — they'll tell you Salt can't do it natively. Our architecture was built from day one to solve the problems Salt still can't.",
    },
    {
      q: "We need a vendor with a large team for enterprise support.",
      a: "Our 38-person team includes the founding engineers of Traceable AI (now a $5B company). We've built enterprise API security platforms before. Our focused team means you talk to engineers, not ticket routers.",
    },
  ],
  landmines: [
    "Ask Salt: What exactly happens to our API traffic data once it reaches your SaaS platform? Where is it stored and for how long?",
    "Ask Salt: Can you block an API attack in real-time without us integrating a third-party WAF?",
    "Ask Salt: What's your roadmap for AI agent and MCP server security? When will it be GA?",
    "Ask Salt: Can you show us how your reporting handles 10,000+ endpoints without performance issues?",
  ],
};

const featureMatrix = [
  { feature: "API Discovery", levo: "eBPF kernel-level + agentless + web scanner", salt: "Traffic mirroring", traceable: "Multi-method + eBPF", noname: "Traffic + config analysis", wallarm: "Traffic + external AASM", akto: "Traffic mirroring" },
  { feature: "Runtime Blocking", levo: "Native inline", salt: "3rd-party required", traceable: "Inline option", noname: "Via Akamai WAAP", wallarm: "Core strength", akto: "Newer capability" },
  { feature: "Shift-Left Testing", levo: "CI/CD integrated", salt: "Pre-production", traceable: "Zero-config from traffic", noname: "150+ dynamic tests", wallarm: "FAST framework", akto: "1,000+ tests" },
  { feature: "AI/Agentic Security", levo: "Full platform (LLM, MCP, RAG, agents)", salt: "Basic MCP monitoring", traceable: "GenAI API security", noname: "Basic", wallarm: "Agentic AI protection", akto: "MCP-first approach" },
  { feature: "Data Privacy", levo: "<1% data leaves env", salt: "Full traffic to SaaS", traceable: "Full data collection", noname: "SaaS-dependent", wallarm: "Hybrid model", akto: "Self-hosted option" },
  { feature: "Deployment Options", levo: "SaaS / hybrid / on-prem / air-gapped", salt: "SaaS only", traceable: "Cloud / on-prem / hybrid", noname: "SaaS / on-prem / hybrid / edge", wallarm: "SaaS / hybrid / on-prem / edge", akto: "SaaS + self-hosted" },
  { feature: "Open Source", levo: "eBPF demo (GPL v3)", salt: "No", traceable: "No", noname: "No", wallarm: "No", akto: "Full MIT license" },
  { feature: "Free Tier", levo: "Limited", salt: "No", traceable: "No", noname: "No", wallarm: "500K req/mo", akto: "Full OSS free" },
  { feature: "Pricing Model", levo: "Per-endpoint, custom", salt: "~$100K/yr per 100M calls", traceable: "Custom enterprise", noname: "Enterprise only", wallarm: "Custom + free tier", akto: "OSS + enterprise" },
];

const activityFeed = [
  { date: "Feb 2026", source: "Salt Security", type: "Product", text: "Announced 12 Months of Innovation campaign with monthly API & AI security releases", sentiment: "threat" },
  { date: "Jan 2026", source: "Levo.ai", type: "Product", text: "Launch week: AI Firewall, AI Gateway, MCP Security, agentless discovery", sentiment: "positive" },
  { date: "Jan 2026", source: "Akto", type: "Product", text: "Launched industry's first MCP Security Platform", sentiment: "threat" },
  { date: "Jul 2025", source: "Wallarm", type: "Funding", text: "Raised $55M Series C for AI-era API security", sentiment: "threat" },
  { date: "Mar 2025", source: "Traceable", type: "M&A", text: "Completed merger with Harness, creating $5B DevSecOps platform", sentiment: "neutral" },
  { date: "Oct 2025", source: "Levo.ai", type: "Product", text: "Launched unified AI Security Platform covering shift-left to runtime", sentiment: "positive" },
];

// ─── Style helpers ───
const pill = (color) => ({
  display: "inline-block",
  padding: "2px 10px",
  borderRadius: 999,
  fontSize: 11,
  fontWeight: 600,
  background: color,
  color: "#fff",
});

const sentimentColors = { threat: "#fecaca", positive: "#bbf7d0", neutral: "#e5e7eb" };
const sentimentText = { threat: "#991b1b", positive: "#166534", neutral: "#374151" };
const typeColors = { Product: "#3b82f6", Funding: "#f59e0b", "M&A": "#8b5cf6" };

// ─── Components ───

function MarketOverview() {
  const maxFunding = Math.max(...competitors.map((c) => c.funding));
  return (
    <div>
      {/* AI Insight Banner */}
      <div style={{ background: "linear-gradient(135deg, #1e1b4b, #312e81)", borderRadius: 12, padding: "16px 20px", marginBottom: 24, color: "#e0e7ff" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 8 }}>
          <span style={{ fontSize: 16 }}>✦</span>
          <span style={{ fontWeight: 700, fontSize: 13, color: "#a5b4fc" }}>AI INSIGHT</span>
        </div>
        <div style={{ fontSize: 14, lineHeight: 1.6 }}>
          Traceable's merger into Harness creates uncertainty for its existing API security customers. 
          <strong style={{ color: "#c7d2fe" }}> Recommendation:</strong> Launch a targeted migration campaign for Traceable customers in fintech and healthcare — 
          Levo's privacy-first architecture directly addresses their top concern about data residency under the new Harness umbrella.
        </div>
      </div>

      {/* Market Stats */}
      <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 12, marginBottom: 24 }}>
        {[
          { label: "Market Size 2025", value: "$1.1B" },
          { label: "Projected 2030", value: "$4.6B" },
          { label: "CAGR", value: "~30%" },
          { label: "API Attacks (2023-24)", value: "150B+" },
        ].map((s) => (
          <div key={s.label} style={{ background: "#f8fafc", borderRadius: 10, padding: "16px", textAlign: "center", border: "1px solid #e2e8f0" }}>
            <div style={{ fontSize: 24, fontWeight: 800, color: "#1e293b" }}>{s.value}</div>
            <div style={{ fontSize: 11, color: "#64748b", marginTop: 4 }}>{s.label}</div>
          </div>
        ))}
      </div>

      {/* Funding Comparison */}
      <div style={{ marginBottom: 24 }}>
        <h3 style={{ fontSize: 14, fontWeight: 700, marginBottom: 12, color: "#334155" }}>Competitor Funding Comparison</h3>
        <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
          {competitors.sort((a, b) => b.funding - a.funding).map((c) => (
            <div key={c.name} style={{ display: "flex", alignItems: "center", gap: 12 }}>
              <div style={{ width: 130, fontSize: 12, fontWeight: 600, color: "#334155", textAlign: "right", flexShrink: 0 }}>{c.name}</div>
              <div style={{ flex: 1, background: "#f1f5f9", borderRadius: 6, height: 24, overflow: "hidden" }}>
                <div style={{ width: `${(c.funding / maxFunding) * 100}%`, background: c.color, height: "100%", borderRadius: 6, minWidth: 2, transition: "width 0.5s" }} />
              </div>
              <div style={{ width: 50, fontSize: 12, color: "#64748b", flexShrink: 0 }}>${c.funding}M</div>
            </div>
          ))}
        </div>
      </div>

      {/* Timeline */}
      <div>
        <h3 style={{ fontSize: 14, fontWeight: 700, marginBottom: 12, color: "#334155" }}>Industry Consolidation Timeline</h3>
        <div style={{ borderLeft: "2px solid #cbd5e1", paddingLeft: 20, display: "flex", flexDirection: "column", gap: 12 }}>
          {marketData.timeline.map((t, i) => (
            <div key={i} style={{ position: "relative" }}>
              <div style={{ position: "absolute", left: -27, top: 4, width: 12, height: 12, borderRadius: "50%", background: t.event.includes("Levo") ? "#3b82f6" : "#94a3b8", border: "2px solid #fff" }} />
              <div style={{ fontSize: 11, fontWeight: 700, color: "#64748b" }}>{t.year}</div>
              <div style={{ fontSize: 13, color: "#334155" }}>{t.event}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

function BattleCardView() {
  const [openObj, setOpenObj] = useState(null);
  return (
    <div>
      {/* Header */}
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 20 }}>
        <div>
          <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 4 }}>
            <span style={{ fontSize: 20, fontWeight: 800, color: "#1e293b" }}>vs. Salt Security</span>
            <span style={pill("#ef4444")}>PRIMARY THREAT</span>
          </div>
          <div style={{ fontSize: 13, color: "#64748b" }}>{battleCard.tagline}</div>
        </div>
        <div style={{ textAlign: "right", fontSize: 12, color: "#64748b", lineHeight: 1.8 }}>
          <div><strong>Funding:</strong> {battleCard.funding}</div>
          <div><strong>Team:</strong> {battleCard.employees} · {battleCard.hq}</div>
          <div><strong>Customers:</strong> {battleCard.customers}</div>
        </div>
      </div>

      {/* Two columns: Weaknesses & How We Win */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16, marginBottom: 20 }}>
        <div>
          <div style={{ fontSize: 12, fontWeight: 700, color: "#991b1b", marginBottom: 8, textTransform: "uppercase", letterSpacing: 0.5 }}>⬇ Where Salt Falls Short</div>
          <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
            {battleCard.weaknesses.map((w, i) => (
              <div key={i} style={{ background: "#fef2f2", borderRadius: 8, padding: "10px 12px", borderLeft: "3px solid #fca5a5" }}>
                <div style={{ fontSize: 13, fontWeight: 700, color: "#991b1b" }}>{w.point}</div>
                <div style={{ fontSize: 12, color: "#7f1d1d", marginTop: 2 }}>{w.detail}</div>
              </div>
            ))}
          </div>
        </div>
        <div>
          <div style={{ fontSize: 12, fontWeight: 700, color: "#166534", marginBottom: 8, textTransform: "uppercase", letterSpacing: 0.5 }}>⬆ How Levo Wins</div>
          <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
            {battleCard.howWeWin.map((w, i) => (
              <div key={i} style={{ background: "#f0fdf4", borderRadius: 8, padding: "10px 12px", borderLeft: "3px solid #86efac" }}>
                <div style={{ fontSize: 13, fontWeight: 700, color: "#166534" }}>{w.point}</div>
                <div style={{ fontSize: 12, color: "#14532d", marginTop: 2 }}>{w.detail}</div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Objection Handling */}
      <div style={{ marginBottom: 20 }}>
        <div style={{ fontSize: 12, fontWeight: 700, color: "#1e40af", marginBottom: 8, textTransform: "uppercase", letterSpacing: 0.5 }}>💬 Objection Handling</div>
        <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
          {battleCard.objections.map((o, i) => (
            <div key={i} style={{ background: "#eff6ff", borderRadius: 8, overflow: "hidden", border: "1px solid #bfdbfe" }}>
              <div
                onClick={() => setOpenObj(openObj === i ? null : i)}
                style={{ padding: "10px 14px", cursor: "pointer", display: "flex", justifyContent: "space-between", alignItems: "center" }}
              >
                <div style={{ fontSize: 13, fontWeight: 600, color: "#1e3a5f" }}>Q: "{o.q}"</div>
                <span style={{ fontSize: 12, color: "#64748b", flexShrink: 0, marginLeft: 8 }}>{openObj === i ? "▲" : "▼"}</span>
              </div>
              {openObj === i && (
                <div style={{ padding: "0 14px 12px", fontSize: 12, color: "#1e3a5f", lineHeight: 1.6, borderTop: "1px solid #bfdbfe" }}>
                  <div style={{ marginTop: 8 }}><strong>Suggested response:</strong> {o.a}</div>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>

      {/* Landmines */}
      <div>
        <div style={{ fontSize: 12, fontWeight: 700, color: "#92400e", marginBottom: 8, textTransform: "uppercase", letterSpacing: 0.5 }}>💣 Landmines to Plant</div>
        <div style={{ background: "#fffbeb", borderRadius: 8, padding: "12px 14px", border: "1px solid #fde68a" }}>
          <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
            {battleCard.landmines.map((l, i) => (
              <div key={i} style={{ fontSize: 12, color: "#78350f", lineHeight: 1.5 }}>
                <span style={{ fontWeight: 700 }}>→</span> {l}
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

function FeatureMatrixView() {
  const cols = ["levo", "salt", "traceable", "noname", "wallarm", "akto"];
  const colLabels = { levo: "Levo.ai", salt: "Salt", traceable: "Traceable", noname: "Noname", wallarm: "Wallarm", akto: "Akto" };

  const isAdvantage = (feature, col) => {
    const val = feature[col]?.toLowerCase() || "";
    if (col === "levo") return false;
    return val.includes("no") || val.includes("3rd-party") || val.includes("basic") || val.includes("sas only");
  };

  return (
    <div>
      <div style={{ background: "linear-gradient(135deg, #1e1b4b, #312e81)", borderRadius: 12, padding: "14px 18px", marginBottom: 20, color: "#e0e7ff" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 6 }}>
          <span style={{ fontSize: 16 }}>✦</span>
          <span style={{ fontWeight: 700, fontSize: 13, color: "#a5b4fc" }}>AI INSIGHT</span>
        </div>
        <div style={{ fontSize: 13, lineHeight: 1.6 }}>
          Levo leads in <strong style={{ color: "#c7d2fe" }}>data privacy</strong> and <strong style={{ color: "#c7d2fe" }}>AI security breadth</strong>. 
          Key gap to address: <strong style={{ color: "#fca5a5" }}>free tier / open-source adoption</strong> — both Wallarm and Akto offer free entry points that drive developer adoption. 
          Consider launching a community edition to compete for bottom-up adoption.
        </div>
      </div>

      <div style={{ overflowX: "auto" }}>
        <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 12 }}>
          <thead>
            <tr style={{ borderBottom: "2px solid #e2e8f0" }}>
              <th style={{ textAlign: "left", padding: "8px 10px", color: "#64748b", fontWeight: 600, width: 140 }}>Capability</th>
              {cols.map((c) => (
                <th key={c} style={{ textAlign: "left", padding: "8px 6px", fontWeight: 700, color: c === "levo" ? "#3b82f6" : "#334155", background: c === "levo" ? "#eff6ff" : "transparent" }}>
                  {colLabels[c]}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {featureMatrix.map((row, i) => (
              <tr key={i} style={{ borderBottom: "1px solid #f1f5f9" }}>
                <td style={{ padding: "8px 10px", fontWeight: 600, color: "#334155" }}>{row.feature}</td>
                {cols.map((c) => (
                  <td key={c} style={{ padding: "8px 6px", color: c === "levo" ? "#1e40af" : "#475569", background: c === "levo" ? "#eff6ff" : "transparent", fontWeight: c === "levo" ? 600 : 400 }}>
                    {row[c]}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function ActivityFeedView() {
  return (
    <div>
      <div style={{ background: "linear-gradient(135deg, #1e1b4b, #312e81)", borderRadius: 12, padding: "14px 18px", marginBottom: 20, color: "#e0e7ff" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 6 }}>
          <span style={{ fontSize: 16 }}>✦</span>
          <span style={{ fontWeight: 700, fontSize: 13, color: "#a5b4fc" }}>AI INSIGHT</span>
        </div>
        <div style={{ fontSize: 13, lineHeight: 1.6 }}>
          Both Salt and Akto are aggressively investing in AI/MCP security — this is now a <strong style={{ color: "#fca5a5" }}>three-way race</strong> with Levo. 
          Wallarm's $55M raise signals they'll accelerate too. <strong style={{ color: "#c7d2fe" }}>Recommendation:</strong> Prioritize publishing AI security benchmark comparisons and customer case studies in Q1 2026 to establish thought leadership before the market gets crowded.
        </div>
      </div>

      <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
        {activityFeed.map((item, i) => (
          <div key={i} style={{ display: "flex", gap: 12, padding: "12px 14px", borderRadius: 10, background: sentimentColors[item.sentiment], border: `1px solid ${sentimentColors[item.sentiment]}` }}>
            <div style={{ flexShrink: 0, width: 70 }}>
              <div style={{ fontSize: 11, fontWeight: 700, color: "#64748b" }}>{item.date}</div>
              <span style={{ ...pill(typeColors[item.type] || "#6b7280"), marginTop: 4 }}>{item.type}</span>
            </div>
            <div>
              <div style={{ fontSize: 13, fontWeight: 700, color: sentimentText[item.sentiment] }}>{item.source}</div>
              <div style={{ fontSize: 12, color: sentimentText[item.sentiment], marginTop: 2 }}>{item.text}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function AIAdvisorView() {
  const [scenario, setScenario] = useState("");
  const [response, setResponse] = useState(null);

  const demoScenarios = [
    { label: "Fintech prospect comparing Salt & Levo", response: "For fintech prospects, lead with data residency — financial regulators increasingly require API traffic data to stay within the customer's boundary. Salt sends full traffic to their SaaS cloud, which creates compliance risk. Open with: 'Can you walk me through your data residency requirements?' Then demonstrate Levo's <1% data architecture. Follow up by planting the landmine: ask the prospect to request Salt's SOC 2 data flow diagram showing where API traffic is stored." },
    { label: "Enterprise evaluating Traceable vs Levo", response: "The Traceable merger with Harness is your biggest lever. Enterprise buyers hate platform uncertainty. Key talking points: (1) Traceable is now a feature inside a DevOps platform, not a focused API security company, (2) Their API security roadmap is now competing with CI/CD, feature flags, and other Harness priorities for resources, (3) Levo's founders literally built Traceable's core technology and then designed a better architecture. Ask: 'Has Traceable confirmed their dedicated API security team size post-merger?'" },
    { label: "Mid-market company looking at free/open-source options", response: "Akto and Wallarm's free tiers are real threats at the mid-market. Don't fight on price — reframe the conversation around total cost. Key angle: free tools require significant internal engineering time to deploy, tune, and maintain. Calculate the prospect's fully-loaded cost of one security engineer's time on setup and ongoing management. Then show Levo's time-to-value: eBPF deployment with zero code changes, automated API discovery, and managed security intelligence. The question to ask: 'How much engineering time are you budgeting for setting up and maintaining your API security tooling?'" },
  ];

  return (
    <div>
      <div style={{ background: "linear-gradient(135deg, #1e1b4b, #312e81)", borderRadius: 16, padding: "24px", marginBottom: 24, color: "#e0e7ff" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 12 }}>
          <span style={{ fontSize: 20 }}>✦</span>
          <span style={{ fontWeight: 800, fontSize: 16, color: "#fff" }}>AI Strategic Advisor</span>
        </div>
        <div style={{ fontSize: 14, lineHeight: 1.6, marginBottom: 16, color: "#c7d2fe" }}>
          Describe a competitive scenario and get a tailored win strategy. Example: "Fintech prospect in Series B, evaluating Salt and Wallarm alongside us."
        </div>
        <div style={{ display: "flex", gap: 8 }}>
          <input
            value={scenario}
            onChange={(e) => setScenario(e.target.value)}
            placeholder="Describe the competitive scenario..."
            style={{ flex: 1, padding: "10px 14px", borderRadius: 8, border: "1px solid #4338ca", background: "#1e1b4b", color: "#e0e7ff", fontSize: 13, outline: "none" }}
          />
          <button
            onClick={() => { if (scenario.trim()) setResponse("This is a demo — in the full product, Claude/OpenAI would generate a tailored strategy based on your scenario, drawing from all competitive intelligence data."); }}
            style={{ padding: "10px 20px", borderRadius: 8, background: "#6366f1", color: "#fff", border: "none", fontWeight: 700, fontSize: 13, cursor: "pointer" }}
          >
            Generate Strategy
          </button>
        </div>
        {response && (
          <div style={{ marginTop: 12, padding: "12px 14px", background: "rgba(255,255,255,0.1)", borderRadius: 8, fontSize: 13, lineHeight: 1.6 }}>
            {response}
          </div>
        )}
      </div>

      <div style={{ fontSize: 12, fontWeight: 700, color: "#334155", marginBottom: 10, textTransform: "uppercase", letterSpacing: 0.5 }}>Pre-built Scenarios</div>
      <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
        {demoScenarios.map((s, i) => (
          <div key={i} style={{ background: "#f8fafc", borderRadius: 10, border: "1px solid #e2e8f0", overflow: "hidden" }}>
            <div
              onClick={() => setResponse(response === s.response ? null : s.response)}
              style={{ padding: "12px 16px", cursor: "pointer", display: "flex", justifyContent: "space-between", alignItems: "center" }}
            >
              <span style={{ fontSize: 13, fontWeight: 600, color: "#1e293b" }}>{s.label}</span>
              <span style={{ fontSize: 12, color: "#6366f1", fontWeight: 600 }}>{response === s.response ? "Hide ▲" : "View Strategy ▼"}</span>
            </div>
            {response === s.response && (
              <div style={{ padding: "0 16px 14px", fontSize: 13, color: "#334155", lineHeight: 1.7, borderTop: "1px solid #e2e8f0" }}>
                <div style={{ marginTop: 10 }}>{s.response}</div>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

// ─── Main App ───
export default function App() {
  const [activeTab, setActiveTab] = useState(1);

  return (
    <div style={{ fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif", maxWidth: 960, margin: "0 auto", padding: "20px 16px", background: "#fff", minHeight: "100vh" }}>
      {/* Header */}
      <div style={{ marginBottom: 20 }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 4 }}>
          <div style={{ width: 32, height: 32, borderRadius: 8, background: "linear-gradient(135deg, #3b82f6, #6366f1)", display: "flex", alignItems: "center", justifyContent: "center", color: "#fff", fontWeight: 800, fontSize: 14 }}>CI</div>
          <span style={{ fontSize: 18, fontWeight: 800, color: "#1e293b" }}>Levo.ai Competitive Intelligence</span>
        </div>
        <div style={{ fontSize: 12, color: "#64748b" }}>API & AI Security Market · Last updated Mar 2026</div>
      </div>

      {/* Tabs */}
      <div style={{ display: "flex", gap: 4, marginBottom: 20, borderBottom: "1px solid #e2e8f0", paddingBottom: 0 }}>
        {TABS.map((tab, i) => (
          <button
            key={tab}
            onClick={() => setActiveTab(i)}
            style={{
              padding: "8px 16px",
              fontSize: 13,
              fontWeight: activeTab === i ? 700 : 500,
              color: activeTab === i ? "#3b82f6" : "#64748b",
              background: "transparent",
              border: "none",
              borderBottom: activeTab === i ? "2px solid #3b82f6" : "2px solid transparent",
              cursor: "pointer",
              transition: "all 0.15s",
            }}
          >
            {tab}
          </button>
        ))}
      </div>

      {/* Content */}
      <div>
        {activeTab === 0 && <MarketOverview />}
        {activeTab === 1 && <BattleCardView />}
        {activeTab === 2 && <FeatureMatrixView />}
        {activeTab === 3 && <ActivityFeedView />}
        {activeTab === 4 && <AIAdvisorView />}
      </div>
    </div>
  );
}

