import type { Assembly, Geometry, Project, Spec } from "./types";

const BASE_URL = "";

type ApiError = {
  message: string;
  status: number;
};

const handleResponse = async <T,>(response: Response): Promise<T> => {
  if (!response.ok) {
    const payload = (await response.json().catch(() => ({ message: response.statusText }))) as {
      message?: string;
    };
    throw { message: payload.message ?? response.statusText, status: response.status } satisfies ApiError;
  }
  return (await response.json()) as T;
};

export const createProject = async (project: Omit<Project, "id" | "updatedAt">): Promise<Project> => {
  const response = await fetch(`${BASE_URL}/projects`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(project),
  });
  return handleResponse<Project>(response);
};

export const fetchProject = async (id: string): Promise<Project> => {
  const response = await fetch(`${BASE_URL}/projects/${id}`);
  return handleResponse<Project>(response);
};

export const updateProject = async (id: string, project: Partial<Project>): Promise<Project> => {
  const response = await fetch(`${BASE_URL}/projects/${id}`, {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(project),
  });
  return handleResponse<Project>(response);
};

export const submitPrompt = async (id: string, prompt: string): Promise<Spec> => {
  const response = await fetch(`${BASE_URL}/projects/${id}/prompt`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  });
  return handleResponse<Spec>(response);
};

export const validateSpec = async (id: string, spec: Spec): Promise<Spec> => {
  const response = await fetch(`${BASE_URL}/projects/${id}/spec/validate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(spec),
  });
  return handleResponse<Spec>(response);
};

export const generateGeometry = async (id: string): Promise<Geometry> => {
  const response = await fetch(`${BASE_URL}/projects/${id}/geometry`, {
    method: "POST",
  });
  return handleResponse<Geometry>(response);
};

export const listComponents = async (id: string): Promise<Assembly> => {
  const response = await fetch(`${BASE_URL}/projects/${id}/assembly/components`);
  return handleResponse<Assembly>(response);
};

export const alignComponents = async (id: string, payload: Assembly): Promise<Assembly> => {
  const response = await fetch(`${BASE_URL}/projects/${id}/assembly/align`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return handleResponse<Assembly>(response);
};

export const exportCad = async (id: string, format: Geometry["format"]): Promise<Geometry> => {
  const response = await fetch(`${BASE_URL}/projects/${id}/export`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ format }),
  });
  return handleResponse<Geometry>(response);
};
