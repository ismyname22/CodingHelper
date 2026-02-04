export type ProjectStatus = "idle" | "validating" | "success" | "error";

export type Project = {
  id: string;
  name: string;
  description: string;
  targetFormat: "STEP" | "STL";
  status: ProjectStatus;
  updatedAt: string;
};

export type SpecValidation = {
  isValid: boolean;
  warnings: string[];
  errors: string[];
};

export type Spec = {
  shape: string;
  dimensions: Record<string, number>;
  units: "mm" | "cm" | "m";
  validation: SpecValidation;
};

export type Geometry = {
  id: string;
  format: "STEP" | "STL";
  createdAt: string;
  previewUrl?: string;
};

export type Assembly = {
  components: string[];
  anchors: string[];
  placements: string[];
};
