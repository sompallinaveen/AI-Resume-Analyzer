import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

import api from "../api/api";

function ResumeHistory() {
  const [resumes, setResumes] = useState([]);

  const navigate = useNavigate();

  useEffect(() => {
    fetchResumes();
  }, []);

  async function fetchResumes() {
    try {
      const response = await api.get("/resume");

      setResumes(response.data);
    } catch (error) {
      console.error(error);
    }
  }

  async function handleDelete(id) {
    const confirmDelete = window.confirm(
      "Are you sure you want to delete this resume?"
    );

    if (!confirmDelete) return;

    try {
      await api.delete(`/resume/${id}`);

      toast.success("Resume deleted successfully");

      fetchResumes();
    } catch (error) {
      toast.error(
        error.response?.data?.detail ||
          "Failed to delete resume"
      );
    }
  }

  return (
    <div className="min-h-screen bg-slate-100">
      <div className="max-w-5xl mx-auto py-10">

        <h1 className="text-3xl font-bold mb-8">
          Resume History
        </h1>

        <div className="space-y-5">

          {resumes.length === 0 && (
            <div className="bg-white rounded-xl shadow p-6 text-center">
              No resumes uploaded yet.
            </div>
          )}

          {resumes.map((resume) => (
            <div
              key={resume.id}
              className="bg-white rounded-xl shadow p-6 flex justify-between items-center"
            >
              <div>
                <h2 className="text-xl font-semibold">
                  {resume.original_filename}
                </h2>

                <p className="text-gray-500 mt-2">
                  Uploaded:
                  {" "}
                  {new Date(
                    resume.uploaded_at
                  ).toLocaleString()}
                </p>
              </div>

              <div className="flex gap-3">

                <button
                  onClick={() =>
                    navigate(
                      `/analysis?resume_id=${resume.id}`
                    )
                  }
                  className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded-lg"
                >
                  Analyze
                </button>

                <button
                  onClick={() =>
                    handleDelete(resume.id)
                  }
                  className="bg-red-600 hover:bg-red-700 text-white px-5 py-2 rounded-lg"
                >
                  Delete
                </button>

              </div>
            </div>
          ))}

        </div>
      </div>
    </div>
  );
}

export default ResumeHistory;