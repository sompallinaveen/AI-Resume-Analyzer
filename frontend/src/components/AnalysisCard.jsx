function AnalysisCard({ title, children }) {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">
      <h2 className="text-2xl font-bold mb-5 text-slate-800">
        {title}
      </h2>

      {children}
    </div>
  );
}

export default AnalysisCard;