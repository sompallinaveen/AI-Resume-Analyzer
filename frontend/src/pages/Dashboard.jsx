import { useNavigate } from "react-router-dom";

import {
  FaUpload,
  FaHistory,
  FaRobot,
  FaUser,
  FaSignOutAlt,
} from "react-icons/fa";

import DashboardCard from "../components/DashboardCard";
import StatsCard from "../components/StatsCard";
import { useAuth } from "../context/AuthContext";

function Dashboard() {
  const navigate = useNavigate();
  const { logout } = useAuth();

  function handleLogout() {
    logout();
    navigate("/");
  }

  return (
    <div className="min-h-screen bg-slate-100">

      <header className="bg-white shadow">

        <div className="max-w-7xl mx-auto flex justify-between items-center p-6">

          <h1 className="text-3xl font-bold text-blue-600">
            AI Resume Analyzer
          </h1>

          <button
            onClick={handleLogout}
            className="flex items-center gap-2 bg-red-600 text-white px-5 py-2 rounded-lg hover:bg-red-700"
          >
            <FaSignOutAlt />
            Logout
          </button>

        </div>

      </header>

      <main className="max-w-7xl mx-auto p-8">

        <h2 className="text-3xl font-bold mb-8">
          Welcome Back 👋
        </h2>

        {/* Stats */}

        <div className="grid md:grid-cols-3 gap-6 mb-10">

          <StatsCard
            title="Resumes"
            value="1"
            color="text-blue-600"
          />

          <StatsCard
            title="Analyses"
            value="1"
            color="text-green-600"
          />

          <StatsCard
            title="Average ATS"
            value="82%"
            color="text-purple-600"
          />

        </div>

        {/* Actions */}

        <div className="grid md:grid-cols-2 gap-6">

          <DashboardCard
            title="Upload Resume"
            description="Upload a new PDF resume."
            path="/upload"
            icon={<FaUpload />}
          />

          <DashboardCard
            title="Resume History"
            description="View all uploaded resumes."
            path="/history"
            icon={<FaHistory />}
          />

          <DashboardCard
            title="AI Analysis"
            description="Analyze a resume with AI."
            path="/analysis"
            icon={<FaRobot />}
          />

          <DashboardCard
            title="Profile"
            description="Coming Soon"
            path="/dashboard"
            icon={<FaUser />}
          />

        </div>

      </main>

    </div>
  );
}

export default Dashboard;