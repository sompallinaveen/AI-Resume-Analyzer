function SkillBadge({ skill, type }) {
  const styles = {
    matched:
      "bg-green-100 text-green-700 border border-green-300",
    missing:
      "bg-red-100 text-red-700 border border-red-300",
  };

  return (
    <span
      className={`px-4 py-2 rounded-full text-sm font-semibold ${styles[type]}`}
    >
      {skill}
    </span>
  );
}

export default SkillBadge;