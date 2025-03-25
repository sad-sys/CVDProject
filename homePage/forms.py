from django import forms

class PredictionForm(forms.Form):
    # Boolean fields (example row showed True/False)
    CAD_at_base = forms.BooleanField(label='CAD_at_base', required=False)
    ts_Vascular_heart_problems_diagnosed_by_doctor_Instance_0_1 = forms.BooleanField(
        label='ts_Vascular.heart.problems.diagnosed.by.doctor...Instance.0_1',
        required=False
    )
    pmh_Merged_ICD_Z39 = forms.BooleanField(label='pmh_Merged.ICD_Z39', required=False)
    ts_Current_tobacco_smoking_Instance_0_0 = forms.BooleanField(
        label='ts_Current.tobacco.smoking...Instance.0_0',
        required=False
    )
    ts_Type_of_tobacco_currently_smoked_Instance_0_neg7 = forms.BooleanField(
        label='ts_Type.of.tobacco.currently.smoked...Instance.0_neg7',
        required=False
    )
    ts_Type_of_tobacco_currently_smoked_Instance_0_3 = forms.BooleanField(
        label='ts_Type.of.tobacco.currently.smoked...Instance.0_3',
        required=False
    )
    ISS_at_base = forms.BooleanField(label='ISS_at_base', required=False)
    ts_Type_of_accommodation_lived_in_Instance_0_neg7 = forms.BooleanField(
        label='ts_Type.of.accommodation.lived.in...Instance.0_neg7',
        required=False
    )
    ts_Type_of_accommodation_lived_in_Instance_0_5 = forms.BooleanField(
        label='ts_Type.of.accommodation.lived.in...Instance.0_5',
        required=False
    )
    ts_Ethnic_background_Instance_0_4003 = forms.BooleanField(
        label='ts_Ethnic.background...Instance.0_4003',
        required=False
    )
    qrisk_Ethnic_background_Instance_0_4003 = forms.BooleanField(
        label='qrisk_Ethnic.background...Instance.0_4003',
        required=False
    )
    nhc_Ethnic_background_Instance_0_4003 = forms.BooleanField(
        label='nhc_Ethnic.background...Instance.0_4003',
        required=False
    )
    ts_Type_of_accommodation_lived_in_Instance_0_3 = forms.BooleanField(
        label='ts_Type.of.accommodation.lived.in...Instance.0_3',
        required=False
    )
    ts_Type_of_accommodation_lived_in_Instance_0_4 = forms.BooleanField(
        label='ts_Type.of.accommodation.lived.in...Instance.0_4',
        required=False
    )
    ts_Type_of_tobacco_currently_smoked_Instance_0_1 = forms.BooleanField(
        label='ts_Type.of.tobacco.currently.smoked...Instance.0_1',
        required=False
    )
    ts_Type_of_accommodation_lived_in_Instance_0_1 = forms.BooleanField(
        label='ts_Type.of.accommodation.lived.in...Instance.0_1',
        required=False
    )
    ts_Type_of_accommodation_lived_in_Instance_0_2 = forms.BooleanField(
        label='ts_Type.of.accommodation.lived.in...Instance.0_2',
        required=False
    )
    ts_Type_of_tobacco_currently_smoked_Instance_0_2 = forms.BooleanField(
        label='ts_Type.of.tobacco.currently.smoked...Instance.0_2',
        required=False
    )
    ts_Alcohol_intake_frequency_Instance_0_6 = forms.BooleanField(
        label='ts_Alcohol.intake.frequency....Instance.0_6',
        required=False
    )
    ts_Current_tobacco_smoking_Instance_0_2 = forms.BooleanField(
        label='ts_Current.tobacco.smoking...Instance.0_2',
        required=False
    )

    # Float fields
    metabolomics_Apolipoprotein_B = forms.FloatField(
        label='metabolomics_Apolipoprotein.B',
        required=True
    )
    metabolomics_Triglycerides_in_HDL = forms.FloatField(
        label='metabolomics_Triglycerides.in.HDL',
        required=True
    )
    metabolomics_Triglycerides_in_Small_HDL = forms.FloatField(
        label='metabolomics_Triglycerides.in.Small.HDL',
        required=True
    )
    metabolomics_Phospholipids_in_Very_Large_HDL = forms.FloatField(
        label='metabolomics_Phospholipids.in.Very.Large.HDL',
        required=True
    )
    metabolomics_Omega_6_Fatty_Acids = forms.FloatField(
        label='metabolomics_Omega.6.Fatty.Acids',
        required=True
    )
    metabolomics_Polyunsaturated_Fatty_Acids = forms.FloatField(
        label='metabolomics_Polyunsaturated.Fatty.Acids',
        required=True
    )
    metabolomics_Triglycerides_in_LDL = forms.FloatField(
        label='metabolomics_Triglycerides.in.LDL',
        required=True
    )
    metabolomics_Free_Cholesterol_in_Large_HDL = forms.FloatField(
        label='metabolomics_Free.Cholesterol.in.Large.HDL',
        required=True
    )
    metabolomics_Total_Lipids_in_Very_Large_HDL = forms.FloatField(
        label='metabolomics_Total.Lipids.in.Very.Large.HDL',
        required=True
    )
    metabolomics_Clinical_LDL_Cholesterol = forms.FloatField(
        label='metabolomics_Clinical.LDL.Cholesterol',
        required=True
    )
