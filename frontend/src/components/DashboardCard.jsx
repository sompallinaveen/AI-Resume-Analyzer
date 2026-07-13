import { useNavigate } from "react-router-dom";

function DashboardCard({
  title,
  description,
  path,
  icon,
}) {
  const navigate = useNavigate();

  return (
    <div
      onClick={() => navigate(path)}
      className="bg-white rounded-xl shadow-md p-6 cursor-pointer hover:shadow-xl hover:-translate-y-1 transition"
    >
      <div className="text-4xl text-blue-600 mb-4">
        {icon}
      </div>

      <h2 className="text-xl font-semibold">
        {title}
      </h2>

      <p className="text-gray-500 mt-2">
        {description}
      </p>
    </div>
  );
}

export default DashboardCard;