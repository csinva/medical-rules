from os.path import join as oj

import numpy as np
import pandas as pd

'''Helper functions for dataset.py.
To do: 
    - any variable transformations or superfluous vars?
    - outcome vars: HospHeadPosCT, Intub24Head,
                        Neurosurgery, DeathTBI,
                        PosIntFinal, any else...
    - what to do about unknowns/NaNs
    - maybe rename columns to Python style
'''

def rename_tbi_neuro(df):
    """Rename categorical features in the TBI Neuro df
    Returns 
    -------
    df: pd.DataFrame - categorical vars are strings
    """
    # mapping binary variables to just yes and no
    binary0 = {
        0: 'No',
        1: 'Yes',
        np.nan: 'Unknown',
    }
    bool_cols0 = [col for col in df if np.isin(df[col].dropna().unique(), [0, 1]).all()]
    for bool_col in bool_cols0:
        df[bool_col] = df[bool_col].map(binary0)    
    
    # change type of categorical cols to strings
    categorical_cols = [col for col in df.columns.tolist() if col != 'id']
    for col in categorical_cols:
        df[col] = df[col].astype(str)
    
    return df

def rename_tbi_pud(df):
    """Rename categorical features in the TBI PUD df
    Returns
    -------
    df: pd.DataFrame - categorical vars are strings
    """
    # mapping employee values to names
    empl_type = {
        1: 'Nurse Practitioner',
        2: 'Physician Assistant',
        3: 'Resident',
        4: 'Fellow',
        5: 'Faculty',
        np.nan: 'Unknown'
    }
    df['EmplType'] = df['EmplType'].map(empl_type)

    # mapping cert values to names
    cert_type = {
        1: 'Emergency Medicine',
        2: 'Pediatrics',
        3: 'Pediatrics Emergency Medicine',
        4: 'Emergency Medicine and Pediatrics',
        90: 'Other',
        np.nan: 'Unknown'
    }
    df['Certification'] = df['Certification'].map(cert_type)

    # mapping injury mech values to names
    inj_mech = {
        1: 'Motor vehicle collision',
        2: 'Pedestrian struck by moving vehicle',
        3: 'Bicyclist struck by automobile',
        4: 'Bike collision/fall',
        5: 'Other wheeled crash',
        6: 'Fall to ground standing/walking/running',
        7: 'Walked/ran into stationary object',
        8: 'Fall from an elevation',  
        9: 'Fall down stairs', 
        10: 'Sports',
        11: 'Assault',
        12: 'Object struck head - accidental',
        90: 'Other mechanism',
        np.nan: 'Unknown'
    }
    df['InjuryMech'] = df['InjuryMech'].map(inj_mech)

    # mapping binary variables to yes, no or unknown (for not applicable)
    inj_impact_sev = {
        1: 'Low',
        2: 'Moderate',
        3: 'High',
        np.nan: 'Unknown'
    }
    df['High_impact_InjSev'] = df['High_impact_InjSev'].map(inj_impact_sev)

    # mapping binary variables to just yes and no
    binary0 = {
        0: 'No',
        1: 'Yes',
        np.nan: 'Unknown',
    }
    bool_cols0 = [col for col in df if np.isin(df[col].dropna().unique(), [0, 1]).all()]
    for bool_col in bool_cols0:
        df[bool_col] = df[bool_col].map(binary0)

    # mapping binary variables to yes, no or unknown (for not applicable)
    binary1 = {
        0: 'No',
        1: 'Yes',
        92: 'Not applicable',
        np.nan: 'Unknown'
    }    
    bool_cols1 = [col for col in df if np.isin(df[col].dropna().unique(), [0, 1, 92]).all()]
    for bool_col in bool_cols1:
        df[bool_col] = df[bool_col].map(binary1)

    # mapping variables to yes, no, and non/pre verbal - amnesia_verb and ha_verb
    verb = {
        0: 'No',
        1: 'Yes',
        91: 'Pre/Non-verbal',
        np.nan: 'Unknown'
    }  
    bool_cols2 = [col for col in df if np.isin(df[col].dropna().unique(), [0, 1, 91]).all()]
    for bool_col in bool_cols2:
        df[bool_col] = df[bool_col].map(verb)

    # mapping history of LOC
    loc_separate = {
        0: 'No',
        1: 'Yes',
        2: 'Suspected',
        np.nan: 'Unknown'
    }
    df['LOCSeparate'] = df['LOCSeparate'].map(loc_separate)

    # length of lossed consciousness
    loc_len = {
        1: '<5 sec',
        2: '5 sec - 1 min',
        3: '1-5 min',
        4: '>5 min',
        92: 'Not applicable',
        np.nan: 'Unknown'
    }
    df['LocLen'] = df['LocLen'].map(loc_len)
    
    # mapping when seizure occured
    seiz_occur = {
        1: 'Immediately on contact',
        2: 'Within 30 minutes of injury',
        3: '>30 minutes after injury',
        92: 'Not applicable',
        np.nan: 'Unknown'
    }
    df['SeizOccur'] = df['SeizOccur'].map(seiz_occur)
    
    # mapping post trauma seizure length
    seiz_len = {
        1: '<1 min',
        2: '1-5 min',
        3: '5-15 min',
        4: '>15 min',
        92: 'Not applicable',
        np.nan: 'Unknown'
    }
    df['SeizLen'] = df['SeizLen'].map(seiz_len)
    
    # mapping severity of headache
    ha_severity = {
        1: 'Mild',
        2: 'Moderate',
        3: 'Severe',
        92: 'Not applicable',
        np.nan: 'Unknown'
    }
    df['HASeverity'] = df['HASeverity'].map(ha_severity)
    
    # mapping headache start to values
    ha_start = {
        1: 'Before head injury',
        2: 'Within 1 hr of event',
        3: '1-4 hrs after event',
        4: '>4 hrs after event',
        92: 'Not applicable',
        np.nan: 'Unknown'
    }
    df['HAStart'] = df['HAStart'].map(ha_start)
    
    # mapping number of vomiting episodes
    vomit_nbr = {
        1: 'Once',
        2: 'Twice',
        3: '>2 times',
        92: 'Not applicable',
        np.nan: 'Unknown'
    }
    df['VomitNbr'] = df['VomitNbr'].map(vomit_nbr)
    
    # mapping first vomit episode to values
    vomit_start = {
        1: 'Before head injury',
        2: 'Within 1 hr of event',
        3: '1-4 hrs after event',
        4: '>4 hrs after event',
        92: 'Not applicable',
        np.nan: 'Unknown'
    }
    df['VomitStart'] = df['VomitStart'].map(vomit_start)
    
    # mapping last vomit episode to values
    vomit_last = {
        1: '<1 hr before ED',
        2: '1-4 hrs before ED',
        3: '>4 hrs before ED',
        92: 'Not applicable',
        np.nan: 'Unknown'
    }
    df['VomitLast'] = df['VomitLast'].map(vomit_last)
    
    # mapping gcs eye component to values
    gsc_eye = {
        1: 'None',
        2: 'Pain',
        3: 'Verbal',
        4: 'Spontaneous',
        np.nan: 'Unknown'
    }
    df['GCSEye'] = df['GCSEye'].map(gsc_eye)
    
    # mapping gcs verbal component to values
    gsc_verbal = {
        1: 'None',
        2: 'Incomprehensible sounds/moans',
        3: 'Inappropriate words/cries',
        4: 'Confused/cries',
        5: 'Oriented/coos',
        np.nan: 'Unknown'
    }
    df['GCSVerbal'] = df['GCSVerbal'].map(gsc_verbal)
    
    # mapping gcs motor component to values
    gsc_motor = {
        1: 'None',
        2: 'Abnormal extension posturing',
        3: 'Abnormal flexing posturing',
        4: 'Pain withdraws',
        5: 'Localizes pain',
        6: 'Follow commands',
    }
    df['GCSMotor'] = df['GCSMotor'].map(gsc_motor)
    
    # map sfxpalp to values
    sfxpalp = {
        0: 'No',
        1: 'Yes',
        2: 'Unclear',
    }
    df['SFxPalp'] = df['SFxPalp'].map(sfxpalp)
        
    # map hermaloc to values
    hema_loc = {
        1: 'Frontal',
        2: 'Occipital',
        3: 'Parietal/Temporal',
        92: 'Not applicable',
    }
    df['HemaLoc'] = df['HemaLoc'].map(hema_loc)
    
    # mapping hermasize to values
    hema_size = {
        1: 'Small',
        2: 'Medium',
        3: 'Large',
        92: 'Not applicable',
        np.nan: 'Unknown'
    }
    df['HemaSize'] = df['HemaSize'].map(hema_size)
    
    # mapping gender to value
    gender = {
        1: 'Male',
        2: 'Female',
        np.nan: 'Unknown'
    }
    df['Gender'] = df['Gender'].map(gender)
    
    
    # mapping ethnicity to names
    eth = {
        1: 'Hispanic',
        2: 'Non-Hispanic',
        np.nan: 'Unknown'
    }
    df['Ethnicity'] = df['Ethnicity'].map(eth)
    
    # mapping race to names
    races = {
        1: 'White',
        2: 'Black',
        3: 'Asian',
        4: 'American Indian',
        5: 'Pacific Islander',
        90: 'Other',
        np.nan: 'Unknown'
    }
    df['Race'] = df['Race'].map(races)
    
    # mapping ed disposition to names
    ed_disposition = {
        1: 'Home',
        2: 'OR',
        3: 'Admit - general patient',
        4: 'Short-stay\Observation',
        5: 'ICU',
        6: 'Transferred Hospital',
        7: 'AMA',
        8: 'Death in ED',
        90: 'Other',
        np.nan: 'Unknown'
    }
    df['EDDisposition'] = df['EDDisposition'].map(ed_disposition)

    # make all of these columns categorical
    numeric_cols = ['id', 'GCSTotal', 'AgeInMonths', 'AgeinYears']
    categorical_cols = [col for col in df.columns.tolist() if col not in numeric_cols]
    for col in categorical_cols:
        df[col] = df[col].astype(str)

    return df

def one_hot_encode_df(df):
    """Transforms categorical features in dataframe 
    Returns 
    -------
    one_hot_df: pd.DataFrame - categorical vars are one-hot encoded 
    """
    # grab only the outcome and predictors - remove related outcomes
    categorical_cols = [col for col in df.columns.tolist() if df[col].dtype == object]
    one_hot_df = pd.get_dummies(df, columns=categorical_cols)
    
    return one_hot_df
    