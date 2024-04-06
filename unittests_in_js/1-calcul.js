function calculateNumber(type, a, b) {
    switch(type) {
        case "SUM":
            return Math.round(a) + Math.round(b);
        case "SUBTRACT":
            return Math.round(b) - Math.round(a);
        case "DIVIDE":
            if (Math.round(b) === 0) throw new Error("Error");
            return Math.round(a) / Math.round(b);
    }
}

module.exports = calculateNumber