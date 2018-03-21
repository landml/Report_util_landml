
package us.kbase.landcontigfilter;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: AssemblyMetadataResults</p>
 * <pre>
 * Here is the definition of the output of the function.  The output
 * can be used by other SDK modules which call your code, or the output
 * visualizations in the Narrative.  'report_name' and 'report_ref' are
 * special output fields- if defined, the Narrative can automatically
 * render your Report.
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "report_name",
    "report_ref",
    "report_content"
})
public class AssemblyMetadataResults {

    @JsonProperty("report_name")
    private String reportName;
    @JsonProperty("report_ref")
    private String reportRef;
    @JsonProperty("report_content")
    private String reportContent;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("report_name")
    public String getReportName() {
        return reportName;
    }

    @JsonProperty("report_name")
    public void setReportName(String reportName) {
        this.reportName = reportName;
    }

    public AssemblyMetadataResults withReportName(String reportName) {
        this.reportName = reportName;
        return this;
    }

    @JsonProperty("report_ref")
    public String getReportRef() {
        return reportRef;
    }

    @JsonProperty("report_ref")
    public void setReportRef(String reportRef) {
        this.reportRef = reportRef;
    }

    public AssemblyMetadataResults withReportRef(String reportRef) {
        this.reportRef = reportRef;
        return this;
    }

    @JsonProperty("report_content")
    public String getReportContent() {
        return reportContent;
    }

    @JsonProperty("report_content")
    public void setReportContent(String reportContent) {
        this.reportContent = reportContent;
    }

    public AssemblyMetadataResults withReportContent(String reportContent) {
        this.reportContent = reportContent;
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
        return ((((((((("AssemblyMetadataResults"+" [reportName=")+ reportName)+", reportRef=")+ reportRef)+", reportContent=")+ reportContent)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
