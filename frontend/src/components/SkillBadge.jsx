function SkillBadge({ skill, type }) {
  const colors = {
    matched: "bg-green-100 text-green-700",
    missing: "bg-red-100 text-red-700",
  };

  return (
    <span
      className={`px-4 py-2 rounded-full text-sm font-medium ${colors[type]}`}
    >
      {skill}
    </span>
  );
}

export default SkillBadge;