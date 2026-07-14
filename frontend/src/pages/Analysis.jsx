import { useSearchParams } from "react-router-dom";
import { useState } from "react";

import toast from "react-hot-toast";

import "react-circular-progressbar/dist/styles.css";
import {
  CircularProgressbar,
  buildStyles,
} from "react-circular-progressbar";

import api from "../api/api";
import { generateReport } from "../utils/pdfGenerator";

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
      const response = await api.post("/ai/analyze", {
        resume_id: Number(resumeId),
        job_description: jobDescription,
      });

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
          rows={10}
          className="w-full border rounded-xl p-4 bg-white"
          placeholder="Paste Job Description..."
          value={jobDescription}
          onChange={(e) =>
            setJobDescription(e.target.value)
          }
        />

        <div className="flex gap-4 mt-6">

          <button
            onClick={analyzeResume}
            disabled={loading}
            className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl transition"
          >
            {loading
              ? "Analyzing..."
              : "Analyze Resume"}
          </button>

          {result && (
            <button
              onClick={() =>
                generateReport(result, resumeId)
              }
              className="bg-green-600 hover:bg-green-700 text-white px-6 py-3 rounded-xl transition"
            >
              Download PDF
            </button>
          )}

        </div>

        {result && (

          <div className="mt-10 grid grid-cols-1 lg:grid-cols-2 gap-6">

            {/* ATS Score */}

            <div className="lg:col-span-2">

              <AnalysisCard title="ATS Score">

                <div className="w-56 h-56 mx-auto">

                  <CircularProgressbar
                    value={result.similarity_score}
                    text={`${result.similarity_score}%`}
                    styles={buildStyles({
                      pathColor: "#2563eb",
                      textColor: "#2563eb",
                      trailColor: "#e5e7eb",
                      strokeLinecap: "round",
                      textSize: "16px",
                    })}
                  />

                </div>

              </AnalysisCard>

            </div>

            {/* Matched Skills */}

            <AnalysisCard title="Matched Skills">

              <div className="flex flex-wrap gap-3">

                {result.matched_skills.map((skill) => (
                  <SkillBadge
                    key={skill}
                    skill={skill}
                    type="matched"
                  />
                ))}

              </div>

            </AnalysisCard>

            {/* Missing Skills */}

            <AnalysisCard title="Missing Skills">

              <div className="flex flex-wrap gap-3">

                {result.missing_skills.map((skill) => (
                  <SkillBadge
                    key={skill}
                    skill={skill}
                    type="missing"
                  />
                ))}

              </div>

            </AnalysisCard>

            {/* Overall Feedback */}

            <div className="lg:col-span-2">

              <AnalysisCard title="Overall Feedback">

                <p className="leading-7 text-gray-700">
                  {result.overall_feedback}
                </p>

              </AnalysisCard>

            </div>

            {/* Strengths */}

            <AnalysisCard title="Strengths">

              <ul className="space-y-2">

                {result.strengths.map((item, index) => (
                  <li key={index}>
                    ✅ {item}
                  </li>
                ))}

              </ul>

            </AnalysisCard>

            {/* Weaknesses */}

            <AnalysisCard title="Weaknesses">

              <ul className="space-y-2">

                {result.weaknesses.map((item, index) => (
                  <li key={index}>
                    ⚠️ {item}
                  </li>
                ))}

              </ul>

            </AnalysisCard>

            {/* Resume Improvements */}

            <AnalysisCard title="Resume Improvements">

              <ul className="space-y-2">

                {result.resume_improvements.map((item, index) => (
                  <li key={index}>
                    ✔ {item}
                  </li>
                ))}

              </ul>

            </AnalysisCard>

            {/* Interview Questions */}

            <AnalysisCard title="Interview Questions">

              <ol className="list-decimal pl-6 space-y-2">

                {result.interview_questions.map((item, index) => (
                  <li key={index}>
                    {item}
                  </li>
                ))}

              </ol>

            </AnalysisCard>

          </div>

        )}

      </div>
    </div>
  );
}

export default Analysis;