# -*- coding: utf-8 -*-
"""
Sample Report Generator
========================
Demonstrates using MLReportDocx to programmatically compile a complete,
publication-grade Word (.docx) technical report adhering to the 8-chapter
specification.
"""

import os
import sys

# Ensure scripts folder is importable
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

from ml_docx_builder import MLReportDocx

def build_sample():
    out_path = os.path.join(BASE_DIR, "examples", "SAMPLE_ML_ANALYSIS_REPORT.docx")
    builder = MLReportDocx()

    # 1. Cover / Title
    builder.add_title_page(
        title="ANALISIS KODE MACHINE LEARNING",
        subtitle="Optimasi Seleksi Fitur Multi-Objektif Menggunakan Binary Genetic Algorithm (GA)",
        metadata_note="Empat berkas Python, 456 baris kode terverifikasi, 12 tabel analisis data"
    )

    # 2. DAFTAR ISI
    builder.add_toc_header("DAFTAR ISI")
    toc_items = [
        (0, "ALUR BACA KODE", 2),
        (0, "ANALISA KODE", 3),
        (1, "1. Gambaran Umum Berkas dan Dataset", 3),
        (1, "2. main.py", 4),
        (1, "3. ga_core.py", 6),
        (0, "HASIL EKSEKUSI", 8),
        (0, "DIAGRAM ALUR PROSES DAN CONTOH PENGERJAAN LENGKAP", 10),
        (1, "1. Diagram Alur Proses GA", 10),
        (1, "2. Contoh Pengerjaan Simpel Step-by-Step", 11),
        (0, "EVALUASI DAN TEMUAN", 14),
        (0, "EVALUASI LANJUTAN DAN REKOMENDASI PERBAIKAN", 16),
        (0, "KESIMPULAN", 19),
    ]
    for i, (lvl, label, pg) in enumerate(toc_items):
        builder.add_toc_entry(lvl, label, pg, first=(i == 0))

    # 3. Chapter: ALUR BACA KODE
    builder.h1("ALUR BACA KODE")
    builder.para(
        "Sistem seleksi fitur berbasis Binary Genetic Algorithm (GA) ini mengeksekusi pipeline modular untuk mengidentifikasi subset sensor optimal. Alur eksekusi program berlangsung secara berantai:"
    )
    builder.para(
        "main.py main() -> load_dataset() -> ga_core.py init_population() -> Looping 100 Generasi (evaluator.py compute_fitness() -> ga_core.py tournament_selection() -> crossover() -> mutate()) -> exporter.py export_results().",
        bold=True
    )
    builder.para(
        "Ruang pencarian solusi dibentuk oleh kombinasi biner 120 bit, merepresentasikan status keikutsertaan setiap kanal sensor. Total kemungkinan subset fitur adalah 2^120 ≈ 1.329 × 10^36 kombinasi."
    )

    # 4. Chapter: ANALISA KODE
    builder.h1("ANALISA KODE")
    builder.h2("1. Gambaran Umum Berkas dan Dataset")
    builder.para(
        "Arsitektur kode terdiri atas empat berkas modular dengan pembagian tanggung jawab yang jelas. Tabel berikut merangkum inventaris modul sistem:"
    )

    builder.table_caption(1, "Inventaris Berkas Sumber Sistem GA")
    headers = ["Nama Berkas", "Baris", "Kelas / Fungsi Utama", "Peran Arsitektural"]
    rows = [
        ["main.py", "84", "main(), parse_args()", "CLI runner, orkestrasi pipeline input/output"],
        ["ga_core.py", "195", "Population, Chromosome", "Algoritma genetika: inisialisasi, seleksi, rekombinasi"],
        ["evaluator.py", "112", "FitnessEvaluator", "Penghitungan fitness multi-objektif (F1 vs Latency)"],
        ["exporter.py", "65", "export_excel()", "Serialisasi hasil optimasi ke format spreadsheet"],
    ]
    widths = [1.5, 0.8, 2.0, 2.0]
    builder.data_table(headers, rows, widths)

    builder.callout(
        title="Catatan Arsitektur: Isolasi Evaluasi Fitness",
        lines=[
            "Pemisahan modul ga_core.py dari evaluator.py memungkinkan substitusi fungsi objektif tanpa perlu merombak operator genetika dasar.",
            "Desain ini mengisolasi ketergantungan library scikit-learn hanya pada lapisan evaluasi."
        ]
    )

    builder.h2("2. ga_core.py")
    builder.para(
        "Operator persilangan (crossover) mengimplementasikan two-point crossover untuk memelihara blok skema biner yang representatif:"
    )

    sample_code = (
        "def two_point_crossover(parent_a: list, parent_b: list, rng):\n"
        "    size = len(parent_a)\n"
        "    pt1, pt2 = sorted(rng.choice(range(1, size), size=2, replace=False))\n"
        "    child_1 = parent_a[:pt1] + parent_b[pt1:pt2] + parent_a[pt2:]\n"
        "    child_2 = parent_b[:pt1] + parent_a[pt1:pt2] + parent_b[pt2:]\n"
        "    return child_1, child_2"
    )
    builder.code_block("ga_core.py line 85-92", sample_code)

    builder.para(
        "Fungsi two_point_crossover memilih dua titik potong secara acak tanpa pengembalian (replace=False). Segmen di antara kedua titik tersebut dipertukarkan di antara kedua induk, menghasilkan dua kromosom anak."
    )

    # 5. Chapter: HASIL EKSEKUSI
    builder.h1("HASIL EKSEKUSI")
    builder.para(
        "Pengujian algoritma dilakukan pada lingkungan komputasi berstandar dengan dataset sensor_stream.csv (10.000 sampel). Parameter eksekusi: populasi = 50, generasi = 100, probabilitas crossover = 0.85, probabilitas mutasi = 0.02."
    )

    builder.table_caption(2, "Performa Konvergensi GA pada Generasi Tertentu")
    metric_headers = ["Generasi", "Fitness Terbaik", "Jumlah Fitur Terpilih", "F1-Score Fault", "Waktu (s)"]
    metric_rows = [
        ["1", "0.7420", "52", "0.7812", "0.45"],
        ["25", "0.8890", "28", "0.8950", "3.12"],
        ["50", "0.9415", "16", "0.9380", "6.24"],
        ["100", "0.9630", "12", "0.9610", "12.80"],
    ]
    builder.data_table(metric_headers, metric_rows, [1.0, 1.3, 1.5, 1.3, 1.1])

    # 6. Chapter: DIAGRAM ALUR DAN CONTOH PENGERJAAN
    builder.h1("DIAGRAM ALUR PROSES DAN CONTOH PENGERJAAN LENGKAP", page_break=True)
    builder.h2("1. Diagram Alur Proses GA")
    builder.para(
        "Diagram alur proses memodelkan seluruh siklus komputasi heuristik dari pemuatan data mentah hingga seleksi subset fitur terbaik:"
    )
    builder.callout(
        title="Ringkasan 5 Tahap Alur Sistem",
        lines=[
            "1. Inisialisasi: Pembangkitan 50 kromosom acak berdimensi 120 bit.",
            "2. Evaluasi: Pengukuran F1-score dan latensi inferensi masing-masing kromosom.",
            "3. Seleksi: Turnamen 3 arah untuk memilih kandidat induk terbaik.",
            "4. Reproduksi: Persilangan dua titik dan mutasi bit acak.",
            "5. Elitisme: Penyimpanan kromosom terbaik sepanjang generasi."
        ]
    )

    builder.h2("2. Contoh Pengerjaan Simpel Step-by-Step")
    builder.para(
        "Untuk mempermudah pemahaman mekanisme internal algoritma, berikut disajikan simulasi numerik 4 langkah konkret dengan angka riil:"
    )
    builder.numbered(1, "Kromosom Induk A mengaktifkan fitur [1, 4, 8, 12, 19], sedangkan Induk B mengaktifkan fitur [3, 8, 15, 22, 30].", "Inisialisasi Induk: ")
    builder.numbered(2, "Titik potong persilangan terpilih secara acak pada indeks 2 dan 4.", "Seleksi Titik Crossover: ")
    builder.numbered(3, "Segmen tengah ditukar, menghasilkan Kromosom Anak dengan fitur [1, 4, 15, 22, 19].", "Rekombinasi: ")
    builder.numbered(4, "Fitness kromosom anak meningkat dari 0.7420 menjadi 0.8150 karena penurunan latensi fitur.", "Evaluasi Hasil: ")

    # 7. Chapter: EVALUASI DAN TEMUAN
    builder.h1("EVALUASI DAN TEMUAN")
    builder.table_caption(3, "Temuan Teknis dan Kualitas Kode")
    f_headers = ["ID", "Kategori", "Deskripsi Temuan", "Dampak pada Sistem"]
    f_rows = [
        ["T-01", "Reproducibility", "Tidak ada penetapan random seed eksplisit pada ga_core.py", "Hasil berbeda pada setiap run"],
        ["T-02", "Komputasi", "Fitness dihitung ulang untuk kromosom yang tidak bermutasi", "Pemborosan siklus CPU 35%"],
        ["T-03", "Diversitas", "Populasi konvergen prematur pada generasi ke-45", "Terjebak pada lokal optimum"],
    ]
    builder.data_table(f_headers, f_rows, [0.8, 1.4, 2.3, 1.8])

    # 8. Chapter: EVALUASI LANJUTAN DAN REKOMENDASI PERBAIKAN
    builder.h1("EVALUASI LANJUTAN DAN REKOMENDASI PERBAIKAN", page_break=True)
    builder.para(
        "Berdasarkan temuan di atas, diusulkan penerapan mekanisme Fitness Caching dan Adaptive Mutation Rate. Berikut cuplikan patch solusi:"
    )
    patch_code = (
        "# Patch T-02: Fitness Caching Decorator\n"
        "fitness_cache = {}\n"
        "def cached_eval(chromosome_tuple):\n"
        "    if chromosome_tuple not in fitness_cache:\n"
        "        fitness_cache[chromosome_tuple] = compute_expensive_fitness(chromosome_tuple)\n"
        "    return fitness_cache[chromosome_tuple]"
    )
    builder.code_block("evaluator.py patch T-02", patch_code)

    builder.table_caption(4, "Hasil Uji Perbandingan Baseline vs Setelah Patch (5 Seed)")
    cmp_headers = ["Metrik Pengujian", "Baseline (5 Seed)", "Setelah Patch (5 Seed)", "Peningkatan"]
    cmp_rows = [
        ["Fitness Rata-rata", "0.9412 ± 0.031", "0.9685 ± 0.008", "+2.9% (Lebih Stabil)"],
        ["Waktu Eksekusi (s)", "18.4 ± 1.2 s", "9.8 ± 0.6 s", "-46.7% (Lebih Cepat)"],
        ["Evaluasi Redundan", "1.750 evaluasi", "0 evaluasi", "100% Tereliminasi"],
    ]
    builder.data_table(cmp_headers, cmp_rows, [1.6, 1.5, 1.5, 1.6])

    # 9. Chapter: KESIMPULAN
    builder.h1("KESIMPULAN")
    builder.para(
        "Analisis mendalam terhadap sistem seleksi fitur Binary GA ini membuktikan efektivitas metode dalam mereduksi 90% dimensi sensor (dari 120 menjadi 12 fitur) dengan tetap mempertahankan akurasi deteksi F1 di atas 0.96. Implementasi patch caching dan adaptive mutation berhasil memangkas waktu inferensi optimasi hingga 46,7% serta menjamin reproduksibilitas penuh."
    )

    builder.save(out_path)
    return out_path

if __name__ == "__main__":
    build_sample()
