
package us.kbase.reportutillandml;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: DomainReportParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "domain_annotation_input_ref",
    "evalue_cutoff",
    "workspace_name",
    "report_format"
})
public class DomainReportParams {

    @JsonProperty("domain_annotation_input_ref")
    private String domainAnnotationInputRef;
    @JsonProperty("evalue_cutoff")
    private Double evalueCutoff;
    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("report_format")
    private String reportFormat;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("domain_annotation_input_ref")
    public String getDomainAnnotationInputRef() {
        return domainAnnotationInputRef;
    }

    @JsonProperty("domain_annotation_input_ref")
    public void setDomainAnnotationInputRef(String domainAnnotationInputRef) {
        this.domainAnnotationInputRef = domainAnnotationInputRef;
    }

    public DomainReportParams withDomainAnnotationInputRef(String domainAnnotationInputRef) {
        this.domainAnnotationInputRef = domainAnnotationInputRef;
        return this;
    }

    @JsonProperty("evalue_cutoff")
    public Double getEvalueCutoff() {
        return evalueCutoff;
    }

    @JsonProperty("evalue_cutoff")
    public void setEvalueCutoff(Double evalueCutoff) {
        this.evalueCutoff = evalueCutoff;
    }

    public DomainReportParams withEvalueCutoff(Double evalueCutoff) {
        this.evalueCutoff = evalueCutoff;
        return this;
    }

    @JsonProperty("workspace_name")
    public String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public DomainReportParams withWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("report_format")
    public String getReportFormat() {
        return reportFormat;
    }

    @JsonProperty("report_format")
    public void setReportFormat(String reportFormat) {
        this.reportFormat = reportFormat;
    }

    public DomainReportParams withReportFormat(String reportFormat) {
        this.reportFormat = reportFormat;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((("DomainReportParams"+" [domainAnnotationInputRef=")+ domainAnnotationInputRef)+", evalueCutoff=")+ evalueCutoff)+", workspaceName=")+ workspaceName)+", reportFormat=")+ reportFormat)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
