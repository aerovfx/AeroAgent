// In a Result component
<table>
  <thead><tr><th>Criterion</th><th>Score</th></tr></thead>
  <tbody>
    {Object.entries(result.scores).map(([key, value]) => (
      <tr key={key}><td>{key}</td><td>{value}</td></tr>
    ))}
  </tbody>
</table>