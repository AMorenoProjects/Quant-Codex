// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
//@version=6
indicator("Screener Z-Score Tecnológicas v6", overlay=true)

// 1. PARÁMETROS
length = input.int(20, "Periodo Media y Volatilidad (N)")
z_threshold = input.float(2.0, "Umbral Z-Score (+/-)")

// Lista extendida de acciones tecnológicas (11 activos)
symbols_input = input.string("NASDAQ:AAPL, NASDAQ:MSFT, NASDAQ:GOOGL, NASDAQ:AMZN, NASDAQ:NVDA, NASDAQ:META, NASDAQ:AMD, NASDAQ:TSLA, NASDAQ:NFLX, NASDAQ:AVGO, NASDAQ:ADBE", "Activos (separados por coma)")

// 2. LÓGICA MATEMÁTICA NÚCLEO
get_zscore(sym, len) =>
    [c, s, d] = request.security(sym, timeframe.period, [close, ta.sma(close, len), ta.stdev(close, len)])
    z = d == 0 ? 0.0 : (c - s) / d
    z

get_color(z, threshold) =>
    z > threshold ? color.new(color.red, 30) : 
      z < -threshold ? color.new(color.green, 30) : 
      color.new(color.gray, 80)

// 3. PREPARACIÓN DE ARRAYS (Motor Dinámico v6)
var symbols = str.split(symbols_input, ",")
var tbl = table.new(position.top_right, 2, array.size(symbols) + 1, frame_color=color.black, frame_width=1, border_color=color.black, border_width=1)

float[] z_scores = array.new_float(0)
string[] clean_symbols = array.new_string(0)

for sym in symbols
    clean_sym = str.trim(sym)
    array.push(clean_symbols, clean_sym)
    z = get_zscore(clean_sym, length)
    array.push(z_scores, z)

// 4. CONSTRUCCIÓN DE INTERFAZ
if barstate.islast
    table.cell(tbl, 0, 0, "Activo", bgcolor=color.black, text_color=color.white)
    table.cell(tbl, 1, 0, "Z-Score", bgcolor=color.black, text_color=color.white)
    
    for i = 0 to array.size(clean_symbols) - 1
        sym = array.get(clean_symbols, i)
        z = array.get(z_scores, i)
        
        table.cell(tbl, 0, i + 1, sym, bgcolor=color.new(color.gray, 80), text_color=color.white)
        table.cell(tbl, 1, i + 1, str.tostring(z, "#.##"), bgcolor=get_color(z, z_threshold), text_color=color.white)