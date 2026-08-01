const { Client } = require('pg');

async function tryConnect(config, label) {
  const client = new Client(config);
  try {
    await client.connect();
    console.log(`SUCCESS with ${label}`);
    const res = await client.query("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name");
    console.log('=== TABLES ===');
    for (const row of res.rows) {
      console.log(row.table_name);
    }
    console.log('\n=== SAMPLE DATA (first 5 rows per table) ===');
    for (const row of res.rows) {
      const tname = row.table_name;
      console.log(`\n--- ${tname} ---`);
      try {
        const r = await client.query(`SELECT * FROM "${tname}" LIMIT 5`);
        if (r.rows.length === 0) {
          console.log('(empty)');
        } else {
          console.log(JSON.stringify(r.rows, null, 2));
        }
      } catch (e) {
        console.log(`Error: ${e.message}`);
      }
    }
    await client.end();
    process.exit(0);
  } catch (e) {
    console.log(`FAILED ${label}: ${e.message}`);
    await client.end();
  }
}

async function main() {
  // Try with original user
  await tryConnect({ host: '192.168.1.157', port: 5432, database: 'mfg_kpi', user: 'admin@mfg_kpi', password: 'Axcend123' }, 'admin@mfg_kpi');
  // Try with just admin
  await tryConnect({ host: '192.168.1.157', port: 5432, database: 'mfg_kpi', user: 'admin', password: 'Axcend123' }, 'admin');
}

main().catch(e => { console.error(e); process.exit(1); });
