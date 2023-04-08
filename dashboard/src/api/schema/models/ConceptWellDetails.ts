/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

import type { BlankEnum } from './BlankEnum';
import type { ExtensionSectionMudTypeEnum } from './ExtensionSectionMudTypeEnum';
import type { MetoceanDataEnum } from './MetoceanDataEnum';
import type { PnaEnum } from './PnaEnum';
import type { Type357Enum } from './Type357Enum';
import type { WellSeasonEnum } from './WellSeasonEnum';

export type ConceptWellDetails = {
    readonly id: number;
    name: string;
    type: Type357Enum;
    top_hole: PnaEnum;
    transport_section: PnaEnum;
    reservoir_section: PnaEnum;
    completion: PnaEnum;
    pna: PnaEnum;
    season: WellSeasonEnum;
    water_depth: number;
    metocean_data: MetoceanDataEnum;
    metocean_days_above_hs_5: number;
    planned_time_per_well?: number | null;
    tvd_from_msl: number;
    md_from_msl?: number | null;
    expected_reservoir_pressure?: number | null;
    expected_reservoir_temperature?: number | null;
    top_hole_section_hole_size?: number | null;
    surface_casing_section_hole_size?: number | null;
    intermediate_casing_section_hole_size?: number | null;
    production_casing_section_hole_size?: number | null;
    extension_section_hole_size?: number | null;
    intermediate_casing_section_mud_type?: (ExtensionSectionMudTypeEnum | BlankEnum);
    production_casing_section_mud_type?: (ExtensionSectionMudTypeEnum | BlankEnum);
    extension_section_mud_type?: (ExtensionSectionMudTypeEnum | BlankEnum);
    intermediate_casing_section_mud_density?: number | null;
    production_casing_section_mud_density?: number | null;
    extension_section_mud_density?: number | null;
    conductor_size?: number | null;
    conductor_weight?: number | null;
    conductor_tvd_shoe_depth?: number | null;
    conductor_md_shoe_depth?: number | null;
    surface_casing_size?: number | null;
    surface_casing_weight?: number | null;
    surface_casing_tvd_shoe_depth?: number | null;
    surface_casing_md_shoe_depth?: number | null;
    intermediate_casing_size?: number | null;
    intermediate_casing_weight?: number | null;
    intermediate_casing_tvd_shoe_depth?: number | null;
    intermediate_casing_md_shoe_depth?: number | null;
    production_casing_size?: number | null;
    production_casing_weight?: number | null;
    production_casing_tvd_shoe_depth?: number | null;
    production_casing_md_shoe_depth?: number | null;
    liner_other_size?: number | null;
    liner_other_weight?: number | null;
    liner_other_tvd_shoe_depth?: number | null;
    liner_other_md_shoe_depth?: number | null;
    no_well_to_be_completed: number;
    planned_time_per_completion_operation: number;
    subsea_xmas_tree_size: number;
    xt_weight: number;
    lrp_size: number;
    lrp_weight: number;
    xt_running_tool_size: number;
    xt_running_tool_weight: number;
    readonly created_at: string;
    readonly updated_at: string;
};
