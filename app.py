<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aesthetic Sales Co-Pilot</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <style>
    .glow-active { box-shadow: 0 0 15px rgba(16, 185, 129, 0.35); }
    .badge-roi { background: linear-gradient(135deg, #059669 0%, #10b981 100%); }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col font-sans select-none">

  <!-- TOP HEADER -->
  <header class="bg-slate-900 border-b border-slate-800 px-4 py-3 flex flex-wrap items-center justify-between gap-3">
    <div class="flex items-center space-x-3">
      <div class="bg-emerald-500/20 p-2 rounded-xl text-emerald-400 border border-emerald-500/30">
        <i data-lucide="activity" class="w-6 h-6"></i>
      </div>
      <div>
        <h1 class="font-bold text-lg leading-tight text-white flex items-center gap-2">
          Aesthetic Sales Co-Pilot <span class="text-xs bg-emerald-500/20 text-emerald-300 px-2 py-0.5 rounded-full border border-emerald-500/30">v1.0 Live</span>
        </h1>
        <p class="text-xs text-slate-400" id="headerProductLabel">Cargando producto...</p>
      </div>
    </div>

    <!-- QUICK ROI STRIP -->
    <div class="flex items-center gap-4 bg-slate-950/80 px-4 py-1.5 rounded-xl border border-slate-800 text-xs">
      <div>
        <span class="text-slate-400">Insumo:</span> 
        <span id="statCosto" class="font-bold text-slate-200">$0</span>
      </div>
      <div class="w-px h-4 bg-slate-800"></div>
      <div>
        <span class="text-slate-400">Cobro sugerido:</span> 
        <span id="statPrecio" class="font-bold text-slate-200">$0</span>
      </div>
      <div class="w-px h-4 bg-slate-800"></div>
      <div class="text-emerald-400 font-bold flex items-center gap-1">
        <i data-lucide="trending-up" class="w-3.5 h-3.5"></i>
        <span id="statMargen">+0% ($0 limpios/paciente)</span>
      </div>
    </div>

    <!-- CONTROLS & CONFIG -->
    <div class="flex items-center gap-2">
      <button onclick="openProductModal()" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-semibold flex items-center gap-1.5 border border-slate-700 transition">
        <i data-lucide="package" class="w-4 h-4 text-emerald-400"></i> Mi Producto
      </button>
      <button onclick="openKnowledgeModal()" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-semibold flex items-center gap-1.5 border border-slate-700 transition">
        <i data-lucide="brain-circuit" class="w-4 h-4 text-cyan-400"></i> Entrenar / Métodos
      </button>
    </div>
  </header>

  <!-- METHODOLOGY PILLS & PIPELINE BAR -->
  <section class="bg-slate-900/60 border-b border-slate-800/80 px-4 py-2.5">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-3">
      <!-- Selector de Metodología -->
      <div class="flex items-center gap-1.5 w-full md:w-auto overflow-x-auto pb-1 md:pb-0">
        <span class="text-xs font-medium text-slate-400 mr-1 flex items-center gap-1">
          <i data-lucide="sliders" class="w-3.5 h-3.5"></i> Enfoque:
        </span>
        <button onclick="setMethodology('reverse')" id="btnMetReverse" class="px-3 py-1 text-xs rounded-full font-medium transition border border-emerald-500/40 bg-emerald-500/20 text-emerald-300">
          Reverse Selling
        </button>
        <button onclick="setMethodology('nepq')" id="btnMetNEPQ" class="px-3 py-1 text-xs rounded-full font-medium transition border border-slate-700 bg-slate-800 text-slate-400 hover:text-white">
          NEPQ (Preguntas Dolor)
        </button>
        <button onclick="setMethodology('consultive')" id="btnMetConsultive" class="px-3 py-1 text-xs rounded-full font-medium transition border border-slate-700 bg-slate-800 text-slate-400 hover:text-white">
          Venta Consultiva ROI
        </button>
      </div>

      <!-- PIPELINE: 5 FASES TÁCTILES -->
      <nav id="pipelineNav" class="grid grid-cols-5 gap-1.5 w-full md:w-2/3 max-w-3xl"></nav>
    </div>
  </section>

  <!-- MAIN LIVE WORKSPACE -->
  <main class="flex-1 max-w-7xl w-full mx-auto p-4 grid grid-cols-1 lg:grid-cols-12 gap-4">
    
    <!-- LEFT: THE CUE CARD (QUÉ DECIR EN VIVO) - 8 COLS -->
    <div class="lg:col-span-8 flex flex-col gap-3">
      <div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-xl flex-1 flex flex-col justify-between">
        
        <div>
          <!-- Meta Header Card -->
          <div class="flex items-center justify-between border-b border-slate-800 pb-3 mb-4">
            <div class="flex items-center gap-2">
              <span id="cardPhaseTag" class="px-2.5 py-0.5 rounded-md text-xs font-bold uppercase tracking-wider bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                FASE 1
              </span>
              <span id="cardGoal" class="text-xs font-medium text-slate-400">
                Objetivo: Desarmar la guardia del doctor en 20s
              </span>
            </div>
            <span class="text-xs text-slate-400 flex items-center gap-1 font-mono">
              <i data-lucide="mic" class="w-3.5 h-3.5 text-emerald-400 animate-pulse"></i> LLAMADA EN CURSO
            </span>
          </div>

          <!-- THE SCRIPT CUE -->
          <div class="mb-4">
            <h2 class="text-xs font-semibold tracking-wider text-slate-400 uppercase mb-1">🗣️ Qué Decir Literalmente:</h2>
            <div id="cardScript" class="text-lg md:text-xl font-medium text-slate-100 bg-slate-950/70 p-4 rounded-xl border border-slate-800/80 leading-relaxed">
              Cargando guion adaptado...
            </div>
          </div>

          <!-- PRO TIP / PSICOLOGÍA -->
          <div class="bg-amber-500/10 border border-amber-500/20 rounded-xl p-3 flex items-start gap-2.5 text-amber-300 text-xs leading-snug">
            <i data-lucide="shield-alert" class="w-4 h-4 flex-shrink-0 mt-0.5"></i>
            <div>
              <strong class="font-bold">Regla de oro médica:</strong>
              <span id="cardTip">No presiones. Habla como un colega que resuelve un cuello de botella.</span>
            </div>
          </div>
        </div>

        <!-- CONTROLS: ANTERIOR / SIGUIENTE -->
        <div class="flex items-center justify-between pt-4 mt-4 border-t border-slate-800">
          <button onclick="prevPhase()" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition">
            <i data-lucide="chevron-left" class="w-4 h-4"></i> Fase Anterior
          </button>
          
          <button onclick="nextPhase()" class="px-6 py-2.5 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold rounded-xl text-sm flex items-center gap-2 shadow-lg shadow-emerald-500/20 transition">
            Siguiente Fase <i data-lucide="chevron-right" class="w-4 h-4"></i>
          </button>
        </div>

      </div>
    </div>

    <!-- RIGHT: EMERGENCY OBJECTION PAD (BOTONES DE PÁNICO) - 4 COLS -->
    <div class="lg:col-span-4 flex flex-col gap-3">
      <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl flex-1 flex flex-col">
        
        <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-800">
          <h3 class="font-bold text-sm text-slate-200 flex items-center gap-2">
            <i data-lucide="shield" class="w-4 h-4 text-rose-400"></i> Desarme de Objeciones
          </h3>
          <button onclick="openNewObjectionModal()" class="text-xs text-emerald-400 hover:text-emerald-300 flex items-center gap-1 font-semibold">
            <i data-lucide="plus-circle" class="w-3.5 h-3.5"></i> Añadir
          </button>
        </div>

        <p class="text-xs text-slate-400 mb-2">Toca si el prospecto interrumpe con:</p>
        
        <!-- TACTILE OBJECTION BUTTONS LIST -->
        <div id="objectionsList" class="flex flex-col gap-2 overflow-y-auto max-h-[380px] pr-1"></div>

        <!-- IMPACTO FINANCIERO DINÁMICO TÁCTIL -->
        <div class="mt-auto pt-3 border-t border-slate-800">
          <button onclick="showFinancialModal()" class="w-full py-2.5 px-3 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold rounded-xl text-xs flex items-center justify-center gap-2 shadow-md">
            <i data-lucide="calculator" class="w-4 h-4"></i> Disparar Argumento Financiero / ROI
          </button>
        </div>

      </div>
    </div>

  </main>

  <!-- MODAL: OBJECIÓN EN TIEMPO REAL (DISPARADA POR TOQUE) -->
  <div id="modalObjectionResponse" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
    <div class="bg-slate-900 border border-rose-500/40 rounded-2xl max-w-lg w-full p-5 shadow-2xl relative glow-active">
      <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
        <span id="objModalTag" class="text-xs font-bold px-2 py-0.5 rounded bg-rose-500/20 text-rose-400 border border-rose-500/30">
          Objeción Activada
        </span>
        <button onclick="closeModal('modalObjectionResponse')" class="text-slate-400 hover:text-white">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>
      
      <p class="text-xs text-slate-400 mb-1 font-semibold uppercase">El prospecto dijo:</p>
      <div id="objModalUserSaid" class="text-sm font-semibold text-rose-200 bg-rose-500/10 p-2.5 rounded-lg border border-rose-500/20 mb-4">
        "Estoy muy ocupado, llame después."
      </div>

      <p class="text-xs text-slate-400 mb-1 font-semibold uppercase">🗣️ Di esto inmediatamente (Sin titubear):</p>
      <div id="objModalResponse" class="text-base font-medium text-emerald-200 bg-slate-950 p-4 rounded-xl border border-slate-800 mb-4 leading-relaxed">
        Respuesta táctica...
      </div>

      <button onclick="closeModal('modalObjectionResponse')" class="w-full py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-xl text-xs font-bold transition">
        Entendido (Volver a la Fase)
      </button>
    </div>
  </div>

  <!-- MODAL: CONFIGURAR PRODUCTO -->
  <div id="modalProduct" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl max-w-lg w-full p-5 shadow-2xl">
      <div class="flex items-center justify-between mb-4 border-b border-slate-800 pb-3">
        <h3 class="font-bold text-base text-white flex items-center gap-2">
          <i data-lucide="package" class="w-5 h-5 text-emerald-400"></i> Ficha del Insumo Médico / Estético
        </h3>
        <button onclick="closeModal('modalProduct')" class="text-slate-400 hover:text-white">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <form id="productForm" onsubmit="saveProduct(event)" class="space-y-3 text-xs">
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Nombre del Insumo / Producto:</label>
          <input type="text" id="inpProdName" required class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 text-white focus:border-emerald-500 outline-none">
        </div>

        <div>
          <label class="block text-slate-300 font-semibold mb-1">Dolor Frecuente con la Competencia (¿De qué se queja el doctor?):</label>
          <input type="text" id="inpProdPain" required placeholder="ej: Nódulos por mala reticulación, viales que se demoran 5 días en llegar" class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 text-white focus:border-emerald-500 outline-none">
        </div>

        <div>
          <label class="block text-slate-300 font-semibold mb-1">Alivio / Diferencial Clave de tu Insumo:</label>
          <input type="text" id="inpProdRelief" required placeholder="ej: Pureza BDDE indetectable, despacho en 24h garantizado y registro sanitario" class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 text-white focus:border-emerald-500 outline-none">
        </div>

        <div class="grid grid-cols-2 gap-3 pt-2">
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Costo al Doctor (USD):</label>
            <input type="number" id="inpProdCost" step="0.5" required class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 text-white focus:border-emerald-500 outline-none">
          </div>
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Cobro Sugerido al Paciente (USD):</label>
            <input type="number" id="inpProdPrice" step="0.5" required class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 text-white focus:border-emerald-500 outline-none">
          </div>
        </div>

        <div class="pt-3 flex gap-2">
          <button type="submit" class="flex-1 py-2.5 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold rounded-xl text-xs transition">
            Guardar y Adaptar Todos los Guiones
          </button>
        </div>
      </form>
    </div>
  </div>

  <!-- MODAL: AGREGAR NUEVA OBJECIÓN -->
  <div id="modalNewObjection" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl max-w-md w-full p-5 shadow-2xl">
      <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
        <h3 class="font-bold text-sm text-white flex items-center gap-1.5">
          <i data-lucide="plus-circle" class="w-4 h-4 text-emerald-400"></i> Registrar Nueva Objeción
        </h3>
        <button onclick="closeModal('modalNewObjection')" class="text-slate-400 hover:text-white">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <form id="newObjForm" onsubmit="saveNewObjection(event)" class="space-y-3 text-xs">
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Título Corto del Botón:</label>
          <input type="text" id="inpObjTitle" placeholder="ej: Pide crédito a 60 días" required class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 text-white focus:border-emerald-500 outline-none">
        </div>
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Lo que dijo el doctor:</label>
          <input type="text" id="inpObjPhrase" placeholder="ej: 'Yo solo compro si me das factura a dos meses'" required class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 text-white focus:border-emerald-500 outline-none">
        </div>
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Tu Respuesta de Alivio (Qué responder):</label>
          <textarea id="inpObjResponse" rows="3" placeholder="Respuesta que desactiva la objeción mostrando el costo o beneficio..." required class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2 text-white focus:border-emerald-500 outline-none"></textarea>
        </div>
        <button type="submit" class="w-full py-2 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold rounded-xl transition">
          Guardar en la Bóveda Táctil
        </button>
      </form>
    </div>
  </div>

  <!-- MODAL: ENTRENAR / MÉTODO CON TEXTO -->
  <div id="modalKnowledge" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl max-w-lg w-full p-5 shadow-2xl">
      <div class="flex items-center justify-between mb-3 border-b border-slate-800 pb-2">
        <h3 class="font-bold text-sm text-white flex items-center gap-1.5">
          <i data-lucide="brain-circuit" class="w-4 h-4 text-cyan-400"></i> Entrenar con Texto / Exportar Base
        </h3>
        <button onclick="closeModal('modalKnowledge')" class="text-slate-400 hover:text-white">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <div class="space-y-4 text-xs">
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Crear Guion Personalizado pegando Notas o Metodología:</label>
          <textarea id="inpCustomMethodText" rows="4" placeholder="Pega aquí apuntes de un libro, un guion de un colega o principios clínicos para adaptar los guiones..." class="w-full bg-slate-950 border border-slate-800 rounded-lg p-2.5 text-white focus:border-cyan-400 outline-none"></textarea>
          <button onclick="applyCustomNotes()" class="mt-2 w-full py-2 bg-cyan-600 hover:bg-cyan-500 text-white font-bold rounded-xl transition flex items-center justify-center gap-1.5">
            <i data-lucide="sparkles" class="w-4 h-4"></i> Incorporar Principios a los Guiones
          </button>
        </div>

        <div class="border-t border-slate-800 pt-3 flex gap-2">
          <button onclick="exportDataJSON()" class="flex-1 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg font-semibold flex items-center justify-center gap-1">
            <i data-lucide="download" class="w-3.5 h-3.5"></i> Exportar Cerebro (.JSON)
          </button>
          <label class="flex-1 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg font-semibold flex items-center justify-center gap-1 cursor-pointer text-center">
            <i data-lucide="upload" class="w-3.5 h-3.5"></i> Importar (.JSON)
            <input type="file" id="fileImport" accept=".json" onchange="importDataJSON(event)" class="hidden">
          </label>
        </div>
      </div>
    </div>
  </div>

  <!-- JAVASCRIPT ENGINE -->
  <script>
    // --- ESTADO INICIAL / DEFAULT DATA ---
    const DEFAULT_PRODUCT = {
      name: "Ácido Hialurónico Reticulado Ultra-3",
      pain: "desabastecimiento con el laboratorio y viales que generan nódulos",
      relief: "cero nódulos garantizado por BDDE ultra purificado y despacho en 24h",
      cost: 42,
      price: 190
    };

    const PHASES_INFO = [
      { id: 0, tag: "Fase 1", name: "Apertura y Desarme", goal: "Desarmar guardia del doctor en los primeros 20 segundos" },
      { id: 1, tag: "Fase 2", name: "Descubrimiento", goal: "Diagnosticar los dolores del doctor y su rentabilidad" },
      { id: 2, tag: "Fase 2.5", name: "Confirmación", goal: "Hacer el puente de compromiso antes de prescribir la solución" },
      { id: 3, tag: "Fase 3", name: "Alivio y Objeciones", goal: "Conectar las ventajas al alivio financiero y vacunar dudas" },
      { id: 4, tag: "Fase 4", name: "Cierre y Certeza", goal: "Liderar con certeza el siguiente paso operativo" }
    ];

    const DEFAULT_OBJECTIONS = [
      {
        id: "obj1",
        tag: "⏱️ 'Estoy ocupado / llame luego'",
        phrase: "Estoy ocupado con paciente, llame después.",
        response: "Doctor, sé que está en consulta. Solo dígame en 5 segundos para no insistir: si hoy su mayor molestia con {PRODUCTO} fuera {DOLOR_TIPICO} o el margen por vial, ¿cuál preferiría eliminar? ...y le cuelgo de inmediato."
      },
      {
        id: "obj2",
        tag: "🤝 'Ya tengo mi proveedor'",
        phrase: "Ya le compro todo a mi laboratorio de confianza.",
        response: "Excelente Doctor, y no le pido que los deje. La mayoría de los médicos con los que trabajamos también los usan, pero tienen 3 viales nuestros como segunda línea para pacientes que buscan {ALIVIO_CLAVE} sin el sobreprecio tradicional. ¿Tiene sentido evaluar una alternativa de respaldo?"
      },
      {
        id: "obj3",
        tag: "📧 'Mándame el catálogo por correo'",
        phrase: "Mándame información o catálogo al correo/WhatsApp.",
        response: "Con gusto se lo envío Doctor, pero nuestro portafolio tiene más de 20 referencias. Para no llenarle la bandeja: si le enviara solo la ficha técnica que le garantiza {MARGEN_NETO} de utilidad neta por paciente, ¿tendría 2 minutos mañana a las 8:30 AM para revisarla juntos?"
      },
      {
        id: "obj4",
        tag: "💸 'Está muy caro'",
        phrase: "Se me hace muy caro comparado con otras marcas.",
        response: "Doctor, en medicina estética lo barato sale carísimo en complicaciones. Nuestro costo es de {COSTO}, pero le permite cobrar {PRECIO_SESION} con total tranquilidad clínica. ¿Prefiere ahorrar $5 dólares en un vial dudoso o embolsarse {MARGEN_NETO} limpios con satisfacción total del paciente?"
      }
    ];

    // --- VARIABLES DE ESTADO ---
    let product = JSON.parse(localStorage.getItem('app_seller_product')) || DEFAULT_PRODUCT;
    let objections = JSON.parse(localStorage.getItem('app_seller_objections')) || DEFAULT_OBJECTIONS;
    let currentPhase = 0;
    let currentMethod = 'reverse'; // 'reverse' | 'nepq' | 'consultive'

    // --- CÁLCULOS FINANCIEROS DINÁMICOS ---
    function getFinancials() {
      const cost = parseFloat(product.cost) || 0;
      const price = parseFloat(product.price) || 0;
      const netMargin = Math.max(0, price - cost);
      const marginPct = price > 0 ? ((netMargin / price) * 100).toFixed(0) : 0;
      const weeklyFivePatients = netMargin * 5;
      const monthlyTwentyPatients = netMargin * 20;

      return {
        cost: `$${cost.toFixed(2)} USD`,
        price: `$${price.toFixed(2)} USD`,
        netMarginStr: `$${netMargin.toFixed(2)} USD`,
        marginPctStr: `${marginPct}%`,
        weeklyFive: `$${weeklyFivePatients.toFixed(2)} USD`,
        monthlyTwenty: `$${monthlyTwentyPatients.toFixed(2)} USD`
      };
    }

    // --- MOTOR DE GUIONES DINÁMICOS ---
    function generateScript(phaseIdx, method) {
      const f = getFinancials();
      const pName = product.name;
      const pPain = product.pain;
      const pRelief = product.relief;

      const scripts = {
        reverse: [
          // Fase 0
          `"Doctor, sé que no esperaba mi llamada y probablemente está por entrar a consulta. Le robo 20 segundos exactos: le llamo porque estamos abasteciendo a clínicas estéticas de la zona con <strong>${pName}</strong> para erradicar el problema de <em>${pPain}</em>. Si esto no es un problema prioritario en su cabina hoy, dígamelo con confianza y le cuelgo ahora mismo."`,
          // Fase 1
          `"Doctor, antes de mostrarle nada de <strong>${pName}</strong>: la mayoría de cirujanos me comentan que están frustrados por <em>${pPain}</em>. En su caso particular, ¿ha tenido algún inconveniente similar recientemente o con su proveedor actual todo marcha al 100%?"`,
          // Fase 2 (Puente)
          `"Doctor, déjeme ver si le escuché bien: usted me dice que lo que más le preocupa es <em>${pPain}</em> y que le gustaría ganar más por sesión. Si hubiera una manera comprobada de tener <strong>${pRelief}</strong> dejándole <strong>${f.netMarginStr} netos por paciente</strong>, ¿estaría dispuesto a revisar un lote inicial o preferiría dejarlo pasar?"`,
          // Fase 3
          `"Mire, no somos la marca más barata del mercado. Cada vial le cuesta <strong>${f.cost}</strong>. Pero aquí está el alivio: le garantizamos <strong>${pRelief}</strong>. Mientras otros le cobran casi lo mismo sin certificados, usted cobra <strong>${f.price}</strong> y se queda con <strong>${f.netMarginStr} limpios en 20 minutos</strong>. ¿Tiene sentido tener una segunda opción así de rentable en cabina?"`,
          // Fase 4
          `"Doctor, para comprobar esto en su propia clínica sin riesgo: podemos prepararle el paquete clínico de 5 viales o el pack de 10 con envío bonificado. ¿Cuál prefiere que le despachemos para que le llegue este jueves antes de mediodía?"`
        ],
        nepq: [
          // Fase 0
          `"Hola Doctor, le habla [Tu Nombre] de la línea estética. Sé que está ocupado. La razón puntual de mi llamada es que estamos ayudando a médicos que aplican <strong>${pName}</strong> y están hartos de <em>${pPain}</em>. ¿Estaría abierto a ver cómo otros colegas lo resolvieron o prefiere que no le quite tiempo?"`,
          // Fase 1
          `"Doctor, cuando aplica tratamientos con su línea habitual... ¿qué tan seguido se topa con <em>${pPain}</em>? Y cuando eso pasa, ¿cuánto tiempo o dinero le cuesta corregirlo con el paciente?"`,
          // Fase 2 (Puente)
          `"Entiendo... entonces si no resuelve el tema de <em>${pPain}</em>, seguirá perdiendo margen y arriesgando citas. Supongamos que tuviéramos un insumo con <strong>${pRelief}</strong> que le garantice <strong>${f.netMarginStr}</strong> por consulta... ¿qué impacto tendría eso en su facturación mensual?"`,
          // Fase 3
          `"Exactamente. El alivio real de <strong>${pName}</strong> no es solo técnico con <strong>${pRelief}</strong>, sino que le da certidumbre: 5 pacientes a la semana le representan <strong>${f.weeklyFive}</strong> netos en su bolsillo. La objeción que algunos tienen al inicio es la marca, pero al ver los registros sanitarios se dan cuenta de la seguridad."`,
          // Fase 4
          `"Doctor, basándonos en lo que me dijo, lo más prudente es que evalúe 5 unidades de prueba. Le genero su orden con factura, le llega el jueves y el viernes coordinamos el protocolo de aplicación. ¿Le parece el paso lógico a seguir?"`
        ],
        consultive: [
          // Fase 0
          `"Buenas tardes Doctor. Le llamo directamente para validar si su consultorio califica para el programa de optimización de margen en <strong>${pName}</strong>. ¿Tiene un minuto para contrastar sus números actuales de rentabilidad?"`,
          // Fase 1
          `"Doctor, haciendo números claros: actualmente, ¿cuánto le cuesta el insumo por paciente y cuánto margen neto le está quedando libre tras costos operativos? ¿Siente que <em>${pPain}</em> le está mermando su ganancia real?"`,
          // Fase 2 (Puente)
          `"De acuerdo a lo que me describe, tiene una fuga de rentabilidad por <em>${pPain}</em>. Si le muestro cómo <strong>${pName}</strong> le entrega <strong>${pRelief}</strong> con un margen garantizado del <strong>${f.marginPctStr}</strong>, ¿podríamos agendar su primer despacho hoy?"`,
          // Fase 3
          `"El análisis financiero es sencillo: costo de <strong>${f.cost}</strong>, usted cobra <strong>${f.price}</strong>, ganancia de <strong>${f.netMarginStr} por aplicación</strong>. Con 20 pacientes al mes, su clínica genera <strong>${f.monthlyTwenty} adicionales</strong> sin aumentar sus costos fijos."`,
          // Fase 4
          `"Doctor, procedamos a activar su cuenta profesional. Le despacho el kit de 5 viales hoy mismo para entrega en 24h. Le envío el enlace de pago seguro a su móvil ahora mismo."`
        ]
      };

      return scripts[method][phaseIdx];
    }

    // --- RENDER PIPELINE TABS ---
    function renderPipeline() {
      const nav = document.getElementById('pipelineNav');
      nav.innerHTML = '';

      PHASES_INFO.forEach((p, idx) => {
        const isActive = idx === currentPhase;
        const btn = document.createElement('button');
        btn.onclick = () => setPhase(idx);
        btn.className = `py-2 px-1 rounded-xl text-center transition flex flex-col items-center justify-center border text-[11px] font-semibold leading-tight ${
          isActive 
            ? 'bg-emerald-500/20 border-emerald-500/50 text-emerald-300 shadow-sm' 
            : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-slate-200 hover:bg-slate-800/60'
        }`;
        btn.innerHTML = `
          <span class="text-[9px] uppercase tracking-wider opacity-60">${p.tag}</span>
          <span class="truncate w-full">${p.name}</span>
        `;
        nav.appendChild(btn);
      });
    }

    // --- RENDER CURRENT CARD ---
    function renderCard() {
      const pInfo = PHASES_INFO[currentPhase];
      document.getElementById('cardPhaseTag').textContent = `${pInfo.tag} • ${pInfo.name}`;
      document.getElementById('cardGoal').textContent = `🎯 Objetivo: ${pInfo.goal}`;
      document.getElementById('cardScript').innerHTML = generateScript(currentPhase, currentMethod);
      
      const tips = [
        "Desarme de guardia: tono desapegado, sin prisa, como un profesional de igual a igual.",
        "Escucha el 80% del tiempo. Si el doctor habla de un dolor, profundiza con '¿por qué?'.",
        "No te saltes la confirmación: si el doctor no admite el dolor, no tiene sentido presentar la solución.",
        "Inocula la objeción antes de que la diga. Cita los números financieros con precisión.",
        "Elimina el 'gracias por su compra'. Lidera con autoridad: dale fechas exactas de lo que pasará."
      ];
      document.getElementById('cardTip').textContent = tips[currentPhase];

      // Update header indicators
      const f = getFinancials();
      document.getElementById('headerProductLabel').textContent = `${product.name} • Margen: ${f.marginPctStr}`;
      document.getElementById('statCosto').textContent = f.cost;
      document.getElementById('statPrecio').textContent = f.price;
      document.getElementById('statMargen').textContent = `+${f.marginPctStr} (${f.netMarginStr} netos/paciente)`;

      lucide.createIcons();
    }

    // --- RENDER OBJECTION BUTTONS ---
    function renderObjections() {
      const list = document.getElementById('objectionsList');
      list.innerHTML = '';

      objections.forEach(obj => {
        const btn = document.createElement('button');
        btn.onclick = () => triggerObjection(obj.id);
        btn.className = "w-full text-left p-2.5 bg-slate-950/70 hover:bg-slate-800/80 border border-slate-800 hover:border-rose-500/40 rounded-xl text-xs text-slate-300 hover:text-rose-200 transition flex items-center justify-between group";
        btn.innerHTML = `
          <span class="font-medium truncate mr-2">${obj.tag}</span>
          <i data-lucide="zap" class="w-3.5 h-3.5 text-slate-500 group-hover:text-rose-400 transition flex-shrink-0"></i>
        `;
        list.appendChild(btn);
      });

      lucide.createIcons();
    }

    // --- ACCIONES TÁCTILES ---
    function setPhase(idx) {
      currentPhase = idx;
      renderPipeline();
      renderCard();
    }

    function nextPhase() {
      if (currentPhase < PHASES_INFO.length - 1) {
        setPhase(currentPhase + 1);
      }
    }

    function prevPhase() {
      if (currentPhase > 0) {
        setPhase(currentPhase - 1);
      }
    }

    function setMethodology(m) {
      currentMethod = m;
      ['btnMetReverse', 'btnMetNEPQ', 'btnMetConsultive'].forEach(b => {
        document.getElementById(b).className = "px-3 py-1 text-xs rounded-full font-medium transition border border-slate-700 bg-slate-800 text-slate-400 hover:text-white";
      });

      const activeBtnMap = {
        reverse: 'btnMetReverse',
        nepq: 'btnMetNEPQ',
        consultive: 'btnMetConsultive'
      };
      
      document.getElementById(activeBtnMap[m]).className = "px-3 py-1 text-xs rounded-full font-medium transition border border-emerald-500/40 bg-emerald-500/20 text-emerald-300";
      renderCard();
    }

    function triggerObjection(id) {
      const obj = objections.find(o => o.id === id);
      if (!obj) return;

      const f = getFinancials();
      let resp = obj.response
        .replace(/{PRODUCTO}/g, `<strong>${product.name}</strong>`)
        .replace(/{DOLOR_TIPICO}/g, `<em>${product.pain}</em>`)
        .replace(/{ALIVIO_CLAVE}/g, `<strong>${product.relief}</strong>`)
        .replace(/{COSTO}/g, `<strong>${f.cost}</strong>`)
        .replace(/{PRECIO_SESION}/g, `<strong>${f.price}</strong>`)
        .replace(/{MARGEN_NETO}/g, `<strong>${f.netMarginStr}</strong>`);

      document.getElementById('objModalTag').textContent = obj.tag;
      document.getElementById('objModalUserSaid').textContent = `"${obj.phrase}"`;
      document.getElementById('objModalResponse').innerHTML = resp;
      
      openModal('modalObjectionResponse');
    }

    // --- MODALES Y CRUD ---
    function openModal(id) {
      document.getElementById(id).classList.remove('hidden');
      lucide.createIcons();
    }

    function closeModal(id) {
      document.getElementById(id).classList.add('hidden');
    }

    function openProductModal() {
      document.getElementById('inpProdName').value = product.name;
      document.getElementById('inpProdPain').value = product.pain;
      document.getElementById('inpProdRelief').value = product.relief;
      document.getElementById('inpProdCost').value = product.cost;
      document.getElementById('inpProdPrice').value = product.price;
      openModal('modalProduct');
    }

    function saveProduct(e) {
      e.preventDefault();
      product.name = document.getElementById('inpProdName').value.trim();
      product.pain = document.getElementById('inpProdPain').value.trim();
      product.relief = document.getElementById('inpProdRelief').value.trim();
      product.cost = parseFloat(document.getElementById('inpProdCost').value) || 0;
      product.price = parseFloat(document.getElementById('inpProdPrice').value) || 0;

      localStorage.setItem('app_seller_product', JSON.stringify(product));
      closeModal('modalProduct');
      renderCard();
    }

    function openNewObjectionModal() {
      openModal('modalNewObjection');
    }

    function saveNewObjection(e) {
      e.preventDefault();
      const title = document.getElementById('inpObjTitle').value.trim();
      const phrase = document.getElementById('inpObjPhrase').value.trim();
      const response = document.getElementById('inpObjResponse').value.trim();

      const newObj = {
        id: "obj_" + Date.now(),
        tag: "⚡ " + title,
        phrase: phrase,
        response: response
      };

      objections.unshift(newObj);
      localStorage.setItem('app_seller_objections', JSON.stringify(objections));
      
      document.getElementById('newObjForm').reset();
      closeModal('modalNewObjection');
      renderObjections();
    }

    function openKnowledgeModal() {
      openModal('modalKnowledge');
    }

    function applyCustomNotes() {
      const text = document.getElementById('inpCustomMethodText').value.trim();
      if (!text) return alert("Por favor escribe o pega algún texto.");
      
      product.relief += ` (Enfoque adicional: ${text.substring(0, 45)}...)`;
      localStorage.setItem('app_seller_product', JSON.stringify(product));
      alert("¡Principios incorporados a los guiones en vivo!");
      closeModal('modalKnowledge');
      renderCard();
    }

    function showFinancialModal() {
      const f = getFinancials();
      alert(`📊 IMPACTO FINANCIERO EN VIVO:\n\n• Insumo: ${f.cost}\n• Cobro por sesión: ${f.price}\n• Margen Neto por paciente: ${f.netMarginStr} (${f.marginPctStr})\n• 5 pacientes/semana: ${f.weeklyFive} limpios\n• 20 pacientes/mes: ${f.monthlyTwenty} netos`);
    }

    // --- IMPORTAR / EXPORTAR JSON ---
    function exportDataJSON() {
      const data = { product, objections };
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `cerebro-ventas-estetica-${Date.now()}.json`;
      a.click();
      URL.revokeObjectURL(url);
    }

    function importDataJSON(e) {
      const file = e.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(evt) {
        try {
          const imported = JSON.parse(evt.target.result);
          if (imported.product && imported.objections) {
            product = imported.product;
            objections = imported.objections;
            localStorage.setItem('app_seller_product', JSON.stringify(product));
            localStorage.setItem('app_seller_objections', JSON.stringify(objections));
            renderCard();
            renderObjections();
            alert("¡Cerebro de ventas importado exitosamente!");
            closeModal('modalKnowledge');
          } else {
            alert("El archivo no tiene el formato correcto.");
          }
        } catch (err) {
          alert("Error al leer el archivo JSON.");
        }
      };
      reader.readAsText(file);
    }

    // --- INICIALIZACIÓN ---
    window.addEventListener('DOMContentLoaded', () => {
      renderPipeline();
      renderCard();
      renderObjections();
      lucide.createIcons();
    });
  </script>
</body>
</html>
