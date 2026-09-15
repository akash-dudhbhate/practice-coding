// Lesson 09 — Medium P03: Dashboard with memo widgets
import { useState, useMemo, useCallback, memo } from "react";
const Stats = memo(({ data }) => <div>Stats: {data}</div>);
const Chart = memo(({ data }) => <div>Chart: {data}</div>);
const Table = memo(({ data, onUpdate }) => <div>Table: {data} <button onClick={onUpdate}>Update</button></div>);
function Dashboard() {
  const [statsData, setStatsData] = useState("100 users");
  const [chartData, setChartData] = useState("bar chart");
  const [tableData, setTableData] = useState("5 rows");
  const stats = useMemo(() => statsData, [statsData]);
  const chart = useMemo(() => chartData, [chartData]);
  const updateTable = useCallback(() => setTableData("6 rows"), []);
  return (
    <div>
      <Stats data={stats} />
      <Chart data={chart} />
      <Table data={tableData} onUpdate={updateTable} />
    </div>
  );
}
export default Dashboard;
