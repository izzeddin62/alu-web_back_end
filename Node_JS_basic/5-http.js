const http = require('http');
const fs = require('fs');

const readDb = async (path) => new Promise((resolve, reject) => {
  fs.readFile(path, { encoding: 'utf8' }, (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }
    resolve(data);
  });
});

const app = http.createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.statusCode = 200;
    res.write('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.statusCode = 200;
    const data = await readDb(process.argv[2]);
    let returnText = 'This is the list of our students\n';
    const lines = data.toString().split('\n').filter((line) => line.length > 0).slice(1);
    const fields = lines.map((line) => line.split(','));
    const fieldNames = fields.map((field) => field[3]).flat();
    const uniqueFieldNames = [...new Set(fieldNames)];
    returnText += `Number of students: ${fields.length}\n`;
    uniqueFieldNames.forEach((field, index) => {
      const students = fields.filter((student) => student[3] === field);
      const studentNames = students.map((student) => student[0]);
      if (index === uniqueFieldNames.length - 1) {
        returnText += `Number of students in ${field}: ${students.length}. List: ${studentNames.join(', ')}`;
        return;
      }
      returnText += `Number of students in ${field}: ${students.length}. List: ${studentNames.join(', ')}\n`;
    });
    res.write(returnText);
  } else {
    res.statusCode = 404;
    res.write('This is not a valid path');
  }
  res.end();
});

app.listen(1245);

module.exports = app;
