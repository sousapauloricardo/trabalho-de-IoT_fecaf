CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS 
SELECT device_id, AVG(temp) as avg_temp FROM temperature_readings 
GROUP BY device_id;

CREATE OR REPLACE VIEW leituras_por_hora AS 
SELECT HOUR(ts) as hora, COUNT(*) as contagem FROM temperature_readings 
GROUP BY hora;

CREATE OR REPLACE VIEW temp_max_min_por_dia AS 
SELECT DATE(ts) as data, MAX(temp) as temp_max, MIN(temp) as temp_min FROM temperature_readings 
GROUP BY data;