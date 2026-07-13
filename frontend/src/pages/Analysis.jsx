import { useSearchParams } from "react-router-dom";
import { useState } from "react";
import toast from "react-hot-toast";
import "react-circular-progressbar/dist/styles.css";

import {
  CircularProgressbar,
  buildStyles,
} from "react-circular-progressbar";
import api from "../api/api";
import AnalysisCard from "../components/AnalysisCard";
import SkillBadge from "../components/SkillBadge";

function Analysis() {

  const [searchParams] = useSearchParams();

  const resumeId = searchParams.get("resume_id");

  const [jobDescription, setJobDescription] = useState("");

  const [result, setResult] = useState(null);

  const [loading, setLoading] = useState(false);

  async function analyzeResume() {

    if (!jobDescription.trim()) {

      toast.error("Enter Job Description");

      return;

    }

    setLoading(true);

    try {

      const response = await api.post(
        "/ai/analyze",
        {
          resume_id: Number(resumeId),
          job_description: jobDescription,
        }
      );

      setResult(response.data);

      toast.success("Analysis Completed");

    } catch (error) {

      toast.error(
        error.response?.data?.detail ||
        "Analysis Failed"
      );

    }

    setLoading(false);

  }

  return (

    <div className="min-h-screen bg-slate-100">

      <div className="max-w-6xl mx-auto py-10 px-4">

        <h1 className="text-3xl font-bold mb-8">
          AI Resume Analysis
        </h1>

        <textarea
          rows="10"
          className="w-full border rounded-xl p-4 bg-white"
          placeholder="Paste Job Description..."
          value={jobDescription}
          onChange={(e)=>setJobDescription(e.target.value)}
        />

        <button
          onClick={analyzeResume}
          disabled={loading}
          className="mt-6 bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl"
        >
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>

        {result && (

          <div className="mt-10 space-y-6">

            <AnalysisCard title="ATS Score">

              <div className="text-center">

                <div className="w-40 h-40 mx-auto">

                    <CircularProgressbar
                        value={result.similarity_score}
                        text={`${result.similarity_score}%`}
                        styles={buildStyles({
                          textColor: "#2563eb",
                          pathColor: "#2563eb",
                          trailColor: "#e5e7eb",
                        })}
                     />

              </div>

              </div>

            </AnalysisCard>

            <AnalysisCard title="Matched Skills">

              <div className="flex flex-wrap gap-3">

                {result.matched_skills.map(skill=>(

                  <SkillBadge
                    key={skill}
                    skill={skill}
                    type="matched"
                  />

                ))}

              </div>

            </AnalysisCard>

            <AnalysisCard title="Missing Skills">

              <div className="flex flex-wrap gap-3">

                {result.missing_skills.map(skill=>(

                  <SkillBadge
                    key={skill}
                    skill={skill}
                    type="missing"
                  />

                ))}

              </div>

            </AnalysisCard>

            <AnalysisCard title="AI Feedback">

              <pre className="whitespace-pre-wrap font-sans">

                {result.ai_feedback}

              </pre>

            </AnalysisCard>

          </div>

        )}

      </div>

    </div>

  );

}

export default Analysis;