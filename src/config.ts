// API Configuration
const API_URL = import.meta.env.VITE_API_URL || '';

export const getApiUrl = (endpoint: string): string => {
  // In development, use proxy (empty API_URL)
  // In production, use the full backend URL
  return `${API_URL}${endpoint}`;
};
