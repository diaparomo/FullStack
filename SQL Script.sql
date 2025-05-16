 TABLE [dbo].[customer](
	[customer_id] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[country_code] [varchar](3) NULL,
	[city] [varchar](25) NULL,
	[postal_code] [varchar](15) NULL,
	[customer_type] [varchar](25) NULL,
	[name] [varchar](40) NULL,
	[address1] [varchar](30) NULL,
	[address2] [varchar](30) NULL,
	[address3] [varchar](30) NULL,
	[billing_attention] [varchar](25) NULL,
	[date_created] [datetime] NULL,
	[last_updated] [datetime] NULL,
	[invoice_branch] [varchar](4) NULL,
	[preferred_currency] [varchar](3) NULL,
	[tax_id] [varchar](20) NULL,
	[ar_account_number] [varchar](15) NULL
	
 CONSTRAINT [pk_customer] PRIMARY KEY CLUSTERED 
(
	[customer_id] ASC
)


CREATE TABLE [dbo].[country](
	[country_code] [varchar](3) NOT NULL,
	[description] [varchar](60) NULL,
	[ec] [char](1) NULL
 CONSTRAINT [pk_country] PRIMARY KEY CLUSTERED 
(
	[country_code] ASC
)

CREATE TABLE [dbo].[shipment](
	[shipment_id] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	
	[shipment_number] [int] NOT NULL,
	[shipment_type] [char](1) NULL,
	[service_type] [varchar](2) NULL,
	[hawb_num] [varchar](11) NULL,
	[date_created] [datetime] NULL,
	[last_updated] [datetime] NULL,
	[user_id] [varchar](8) NULL,
	[shipper_customer_id] [int] NULL,
	[consignee_customer_id] [int] NULL,
	[commodity_description] [varchar](25) NULL,
	[number_of_items] [int] NULL,
	[gross_weight] [float] NULL
 CONSTRAINT [pk_shipment] PRIMARY KEY CLUSTERED 
(
	[shipment_id] ASC
	
)

CREATE TABLE [dbo].[invoice](
	[invoice_id] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[invoice_number] [int] NULL,
	[customer_id] [int] NOT NULL,
	[branch_id] [int] NULL,
	[invoice_date] [datetime] NULL,
	[date_created] [datetime] NULL,
	[exchange_date] [datetime] NULL,
	[account_number] [varchar](15) NULL,
	[local_currency_code] [varchar](4) NULL,
	[accounting_period_date] [datetime] NULL,
	[revenue_total] [float] NULL,
	[tax_total] [float] NULL
	
 CONSTRAINT [pk_invoice] PRIMARY KEY CLUSTERED 
(
	[invoice_id] ASC
)



CREATE TABLE [dbo].[revenue](
	[revenue_id] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[shipment_id] [int] NULL,
	[invoice_id] [int] NULL,
	[customer_id] [int] NULL,
	[category_id] [int] NULL,
	[invoice_currency] [varchar](4) NULL,
	[invoice_actual_amount] [float] NULL,
	[invoice_actual_tax_amount] [float] NULL,
	
 CONSTRAINT [pk_revenue] PRIMARY KEY CLUSTERED 
(
	[revenue_id] ASC
)

CREATE TABLE [dbo].[category](
	[category_id] [int] IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
	[description] [varchar](25) NULL,
	
 CONSTRAINT [pk_category] PRIMARY KEY CLUSTERED 
(
	[category_id] ASC,
	
)