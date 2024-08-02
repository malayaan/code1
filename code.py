def apply_flags_on_no_incidents_days(labeliser):
    # Filtrer les incidents qui ne sont pas présents dans les jours sans incidents
    labeliser.df_indicators_no_incident = labeliser.deal_indicators[
        labeliser.deal_indicators["pricingdate"].isin(labeliser.df_no_incident["Incident_date"])
    ]
    
    # Utiliser .loc pour mettre à jour la colonne 'Type' des lignes filtrées
    labeliser.df_indicators_no_incident.loc[
        labeliser.df_indicators_no_incident.index, "Type"
    ] = "NotAnIncident"
