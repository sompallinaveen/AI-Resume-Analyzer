function AnalysisCard({ title, children }) {
  return (
    <div className="bg-white rounded-xl shadow-md p-6">

      <h2 className="text-xl font-bold mb-4">
        {title}
      </h2>

      {children}

    </div>
  );
}

export default AnalysisCard;