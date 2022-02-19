import XCTest
@testable import MergeSort

final class MergeSortTests: XCTestCase {
    static var allTests = [
        ("testAlreadySorted", testAlreadySorted),
    ]
    
    func testAlreadySorted() {
        let linearArray = Array<Int>(0 ... 5)
        
        XCTAssertEqual(MergeSort(linearArray), linearArray)
    }
}
