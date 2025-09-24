import { useState } from 'react';
import axios from 'axios';
import { Button, Upload } from 'antd';

export default function Home() {
  const [hwFile, setHwFile] = useState(null);
  const [rubricFile, setRubricFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleAnalyze = async () => {
    const formData = new FormData();
    formData.append('handwriting', hwFile);
    formData.append('rubric', rubricFile);
    const res = await axios.post('http://localhost:8000/analyze', formData);
    setResult(res.data);
  };

  return (
    <div>
      <Upload onChange={(info) => setHwFile(info.file.originFileObj)}>Upload Handwriting Image</Upload>
      <Upload onChange={(info) => setRubricFile(info.file.originFileObj)}>Upload Rubric Word</Upload>
      <Button onClick={handleAnalyze}>Analyze</Button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}