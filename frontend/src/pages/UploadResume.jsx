import { useState } from "react";
import toast from "react-hot-toast";

import api from "../api/api";

function UploadResume() {

  const [file, setFile] = useState(null);

  const [loading, setLoading] = useState(false);

  const [result, setResult] = useState(null);

  async function handleUpload(e) {

    e.preventDefault();

    if (!file) {

      toast.error("Please select a PDF.");

      return;

    }

    const formData = new FormData();

    formData.append("file", file);

    setLoading(true);

    try {

      const response = await api.post(
        "/resume/upload",
        formData,
        {
          headers: {
            "Content-Type":
              "multipart/form-data",
          },
        }
      );

      setResult(response.data);

      toast.success("Resume Uploaded");

    } catch (error) {

      toast.error(
        error.response?.data?.detail ||
        "Upload Failed"
      );

    }

    setLoading(false);

  }

  return (

    <div className="min-h-screen bg-slate-100">

      <div className="max-w-3xl mx-auto py-10">

        <div className="bg-white rounded-xl shadow-lg p-8">

          <h1 className="text-3xl font-bold mb-8">
            Upload Resume
          </h1>

          <form
            onSubmit={handleUpload}
            className="space-y-5"
          >

            <input
              type="file"
              accept=".pdf"
              onChange={(e)=>setFile(e.target.files[0])}
            />

            <button
              disabled={loading}
              className="bg-blue-600 text-white px-6 py-3 rounded-xl hover:bg-blue-700"
            >
              {loading ? "Uploading..." : "Upload Resume"}
            </button>

          </form>

          {result && (

            <div className="mt-8 bg-green-50 border border-green-200 rounded-xl p-6">

              <h2 className="text-xl font-bold mb-4">
                Upload Successful
              </h2>

              <p><b>Filename:</b> {result.filename}</p>

              <p><b>Words:</b> {result.words}</p>

              <p><b>Characters:</b> {result.characters}</p>

              <div className="mt-4">

                <h3 className="font-semibold mb-2">
                  Skills Found
                </h3>

                <div className="flex flex-wrap gap-2">

                  {result.skills.map(skill=>(

                    <span
                      key={skill}
                      className="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-sm"
                    >
                      {skill}
                    </span>

                  ))}

                </div>

              </div>

            </div>

          )}

        </div>

      </div>

    </div>

  );

}

export default UploadResume;