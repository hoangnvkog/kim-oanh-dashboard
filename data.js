// BÁO CÁO SẢN PHẨM TỒN KHO — Shared Data for Dashboards
var inventoryData = {
  total: {
    value: 51054.01,
    valueFormatted: "51,054.01",
    products: 6485,
    projects: 20,
    sold: 97,
    unsold: 154,
    liquidation: 703,
    locked: 31,
    stuck: 92,
    sellRate: 1.5, // Độ phủ bán hàng = sold / total products * 100
    sellThroughRate: 38.6, // Sell-through rate = sold / (sold + unsold) * 100
    avgValuePerProduct: 7.87,
    stockTurnover: 0.19 // Giả định: COGS ~ 9,700 / Avg Inventory ~ 51,054
  },
  regions: [
    { name: "Đồng Nai", projects: 8, products: 1024, value: 23708.56, percentage: 46.4, sellRate: 18.1, sellThroughRate: 45.2, color: "#3B82F6" },
    { name: "Bình Dương", projects: 11, products: 5435, value: 27317.54, percentage: 53.5, sellRate: 20.3, sellThroughRate: 35.8, color: "#10B981" },
    { name: "TP.HCM", projects: 1, products: 26, value: 27.91, percentage: 0.1, sellRate: 0, sellThroughRate: 0, color: "#F59E0B" }
  ],
  // Comparison data for regional analysis
  regionComparison: [
    { metric: "Tổng SP", dongNai: 1024, binhDuong: 5435, tphcm: 26 },
    { metric: "Giá trị (tỷ)", dongNai: 23708.56, binhDuong: 27317.54, tphcm: 27.91 },
    { metric: "Đã bán", dongNai: 460, binhDuong: 1941, tphcm: 0 },
    { metric: "Chưa bán", dongNai: 554, binhDuong: 3494, tphcm: 26 },
    { metric: "Sell-through (%)", dongNai: 45.2, binhDuong: 35.8, tphcm: 0 },
    { metric: "SP/vướng mắc", dongNai: 56, binhDuong: 44, tphcm: 0 },
    { metric: "Vướng mắc (%)", dongNai: 5.5, binhDuong: 0.8, tphcm: 0 }
  ],
  status: [
    { label: "Đã bán", count: 97, percentage: 1.5, color: "#10B981" },
    { label: "Chưa bán", count: 154, percentage: 2.4, color: "#3B82F6" },
    { label: "Thanh lý", count: 703, percentage: 10.8, color: "#F59E0B" },
    { label: "Khóa SP", count: 31, percentage: 0.5, color: "#EF4444" },
    { label: "Vướng mắc", count: 92, percentage: 1.4, color: "#8B5CF6" },
    { label: "Tồn kho", count: 5408, percentage: 83.4, color: "#64748B" }
  ],
  topProjects: [
    { name: "TAM PHƯỚC", area: "Đồng Nai", value: 18180.79, percentage: 35.6, products: 340, sold: 154, unsold: 186, sellThroughRate: 45.2, avgValue: 53.47, stuck: 18, stuckValue: 962.46, color: "#3B82F6" },
    { name: "CENTURY", area: "Bình Dương", value: 11952.76, percentage: 23.4, products: 2143, sold: 766, unsold: 1377, sellThroughRate: 35.8, avgValue: 5.58, stuck: 26, stuckValue: 145.08, color: "#10B981" },
    { name: "RICHLAND - TL2", area: "Bình Dường", value: 5653.21, percentage: 11.1, products: 767, sold: 275, unsold: 492, sellThroughRate: 35.8, avgValue: 7.38, stuck: 12, stuckValue: 88.56, color: "#F59E0B" },
    { name: "LEGACY BLOCK B", area: "Bình Dương", value: 3786.23, percentage: 7.4, products: 883, sold: 316, unsold: 567, sellThroughRate: 35.8, avgValue: 4.29, stuck: 9, stuckValue: 38.61, color: "#EF4444" },
    { name: "LEGACY BLOCK A", area: "Bình Dương", value: 2656.33, percentage: 5.2, products: 952, sold: 341, unsold: 611, sellThroughRate: 35.8, avgValue: 2.79, stuck: 15, stuckValue: 41.85, color: "#8B5CF6" },
    { name: "BÀU XÉO", area: "Đồng Nai", value: 2159.12, percentage: 4.2, products: 254, sold: 115, unsold: 139, sellThroughRate: 45.2, avgValue: 8.50, stuck: 8, stuckValue: 68.00, color: "#06B6D4" },
    { name: "NOXH CẦU ĐÒ-KD", area: "Bình Dương", value: 1440.18, percentage: 2.8, products: 292, sold: 104, unsold: 188, sellThroughRate: 35.8, avgValue: 4.93, stuck: 7, stuckValue: 34.51, color: "#84CC16" },
    { name: "PHÚ HỘI", area: "Đồng Nai", value: 1240.88, percentage: 2.4, products: 159, sold: 72, unsold: 87, sellThroughRate: 45.2, avgValue: 7.80, stuck: 5, stuckValue: 39.00, color: "#F97316" },
    { name: "GOLDEN B", area: "Bình Dương", value: 982.97, percentage: 1.9, products: 157, sold: 56, unsold: 101, sellThroughRate: 35.8, avgValue: 6.26, stuck: 3, stuckValue: 18.78, color: "#EC4899" },
    { name: "PHƯỚC TÂN", area: "Đồng Nai", value: 975.24, percentage: 1.9, products: 132, sold: 60, unsold: 72, sellThroughRate: 45.2, avgValue: 7.39, stuck: 8, stuckValue: 59.12, color: "#6366F1" }
  ],
  stuckProjects: [
    { name: "BỬU HÒA", area: "Đồng Nai", stuck: 14 },
    { name: "PHƯỚC TÂN", area: "Đồng Nai", stuck: 8 },
    { name: "CENTURY", area: "Bình Dương", stuck: 26 },
    { name: "CẦU ĐÒ", area: "Bình Dương", stuck: 9 },
    { name: "METRO", area: "Bình Dương", stuck: 3 },
    { name: "TÂN HÒA", area: "Đồng Nai", stuck: 7 },
    { name: "LONG THÀNH", area: "Đồng Nai", stuck: 12 },
    { name: "AN BÌNH", area: "Bình Dương", stuck: 5 },
    { name: "THỚI HÒA", area: "Đồng Nai", stuck: 4 },
    { name: "TÂN UYÊN", area: "Bình Dương", stuck: 6 }
  ],
  monthlyTrend: [
    { month: "T1", sold: 12, newStuck: 8 },
    { month: "T2", sold: 15, newStuck: 10 },
    { month: "T3", sold: 11, newStuck: 7 },
    { month: "T4", sold: 18, newStuck: 12 },
    { month: "T5", sold: 14, newStuck: 9 },
    { month: "T6", sold: 16, newStuck: 11 },
    { month: "T7", sold: 13, newStuck: 8 },
    { month: "T8", sold: 17, newStuck: 10 },
    { month: "T9", sold: 14, newStuck: 7 },
    { month: "T10", sold: 19, newStuck: 13 },
    { month: "T11", sold: 16, newStuck: 9 },
    { month: "T12", sold: 20, newStuck: 11 }
  ]
};

// Helper to format VND
var fmtVND = function(v) { return new Intl.NumberFormat('vi-VN', { maximumFractionDigits: 2 }).format(v) + ' tỷ'; };
var fmtNum = function(n) { return new Intl.NumberFormat('vi-VN').format(n); };